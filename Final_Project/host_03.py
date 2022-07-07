from flask import Flask, render_template, request, url_for, redirect,  session, jsonify, flash
import socket
import pickle
import struct
import threading
from flask_socketio import SocketIO

HOST = '127.0.0.1'
PORT = 2021

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
socketio = SocketIO(app)

app.config['SECRET_KEY'] = '36f69927f4425cbf10ae2f5a0acd8372'

s = socket.socket()

s.connect((HOST, PORT))

Response = s.recv(1024)
print(Response)

global dashboard_Item_string, home_data_string, item_data_string

multicast_IP = '224.0.0.3'
Broadcast_Data = {"Type": "No_New_Notification"}
Broadcast_Sub_Data = {"Type": "No_New_Notification"}


def multicasting():
    MCAST_GRP = multicast_IP
    MCAST_PORT = 2022
    IS_ALL_GROUPS = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if IS_ALL_GROUPS:
        sock.bind(('', MCAST_PORT))
    else:
        sock.bind((MCAST_GRP, MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    while True:
        multicast_raw_data = sock.recv(4096)
        multicast_data = pickle.loads(multicast_raw_data)
        print("Multicast_Data:- ", multicast_data)
        Multi_Type = multicast_data["Type"]
        print("Multicast_Type", Multi_Type)

        if Multi_Type == "Broadcast":
            Image = multicast_data["Response"]["Image"]
            Title = multicast_data["Response"]["Title"]
            Base_Price = multicast_data["Response"]["Base_Price"]
            Expiry_Date = multicast_data["Response"]["Expiry_Date"]
            print("Image = ", Image,
                  "Title", Title,
                  "Base_Price", Base_Price,
                  "Expiry_Date", Expiry_Date)
            global Broadcast_Data
            Broadcast_Data = multicast_data["Response"]
            print("Broadcast_Data = ", Broadcast_Data)

        if Multi_Type == "Broadcast_Sub":
            Title = multicast_data["Response"]["Title"]
            Base_Price = multicast_data["Response"]["Base_Price"]
            Max_bid = multicast_data["Response"]["Max_bid"]
            print("Title", Title,
                  "Base_Price", Base_Price,
                  "Max_bid", Max_bid)
            global Broadcast_Sub_Data
            Broadcast_Sub_Data = multicast_data["Response"]
            print("Broadcast_Sub_Data = ", Broadcast_Sub_Data)


mu = threading.Thread(target=multicasting)
mu.start()

while True:
    @socketio.on('disconnect')
    def disconnect_user():
        logout()

    @app.route("/", methods=['GET', 'POST'])
    def index():
        global s
        print("Request_Method = ", request.method)
        if request.method == 'POST':
            if request.form.get('Log_in') == 'Log_in':
                email = request.form.get('email')
                password = request.form.get('password')
                user_login = {'Type': 'Log_In', 'email': email, 'password': password}
                Login_arr = pickle.dumps(user_login)
                s.send(Login_arr)

                user_raw_data = s.recv(4096)
                user_raw_arr = pickle.loads(user_raw_data)
                print("user_raw_arr", user_raw_arr)
                if user_raw_arr["Type"] == "User":
                    user_data_arr = user_raw_arr["Data"]
                    session["email"] = email
                    session['user_data_arr'] = user_data_arr
                    print('User_Data', repr(user_data_arr))

                    User_ID = user_data_arr[0][0]

                    multicasting_request = {'Type': 'Multicasting_Request', "User_ID": User_ID, 'Multicasting_ID': multicast_IP}
                    multicasting_request_Dump = pickle.dumps(multicasting_request)
                    s.send(multicasting_request_Dump)
                    flash("Login successful")

                    return redirect('/')

                if user_raw_arr["Type"] == "Error":
                    print("User invalid")
                    user_data_arr = None
                    session["user_data_arr"] = None
                    print(user_data_arr)
                    #flash("Login unsuccessful. Please try again!")
                    flash(user_raw_arr["Data"])
                    return redirect('/')
                # return redirect(url_for('index', user_data=user_data_arr))

            elif request.form.get('Sign_Up') == 'Sign_Up':
                First_Name = request.form.get('First_Name')
                Last_Name = request.form.get('Last_Name')
                Phone_Number = request.form.get("Phone_Number")
                Email = request.form.get("Email")
                Password = request.form.get("Password")
                Password_Check = request.form.get("Password_Check")

                if Password == Password_Check:
                    user_signup = {'Type': 'Sign_Up', 'First_Name': First_Name, 'Last_Name': Last_Name,
                                   'Phone_Number': Phone_Number, 'Email': Email, 'Password': Password}
                    signup_arr = pickle.dumps(user_signup)
                    s.send(signup_arr)

                    data = s.recv(8096)
                    data_arr = pickle.loads(data)
                    print('Response = ', repr(data_arr))
                    flash(data_arr["Data"])
                    return redirect('/')
                else:
                    flash("password does not match")
                    return redirect('/')

            elif request.form.get('Dashboard') == 'Dashboard':
                return redirect('dashboard')

            elif request.form.get('Item_Bid') == 'Item_Bid':
                print("Item_Bid")
                user_id = request.form.get('User_ID')
                item_id = request.form.get('Item_ID')
                Expiry_Date = request.form.get('Expiry_Date')
                Time_Extended = request.form.get('Time_Extended')
                bid_price = request.form.get('Bid_Price')
                print("bid_price", bid_price, "item_id", item_id, "user_id", user_id)

                bid_data = {'Type': 'Bid', 'User_ID': user_id, 'Item_ID': item_id, 'Expiry_Date': Expiry_Date, 'Time_Extended': Time_Extended, 'Bid_Price': bid_price}
                bid_data_arr = pickle.dumps(bid_data)
                s.send(bid_data_arr)

                data = s.recv(4096)
                bid_data_arr = pickle.loads(data)
                print('Received_Item', repr(bid_data_arr))
                return redirect('item')

            elif request.form.get('Item_Sub') == 'Item_Sub':
                # print("Item_Sub")
                user_id = request.form.get('User_ID')
                item_id = request.form.get('Item_ID')

                bid_data = {'Type': 'Item_Sub', 'User_ID': user_id, 'Item_ID': item_id}
                bid_data_arr = pickle.dumps(bid_data)
                s.send(bid_data_arr)

                data = s.recv(4096)
                sub_data_arr = pickle.loads(data)
                flash(sub_data_arr["Data"])
                return redirect('item')

            elif request.form.get('Item') == 'Item':
                Item_ID = request.form.getlist('Item_ID')
                Item_Category = request.form.getlist('Item_Category')
                print(Item_ID)
                session['Item_ID'] = Item_ID
                session["Item_Category"] = Item_Category
                return redirect(url_for('item', date=Item_ID))

            else:
                global Broadcast_Sub_Data
                user_data_arr = session.get('user_data_arr')
                if user_data_arr is not None:
                    First_Name = user_data_arr[0][1]
                    Last_Name = user_data_arr[0][2]

                    return render_template("home.html", user_data=user_data_arr, First_Name=First_Name, Last_Name=Last_Name)
                else:
                    return render_template("home.html")
        elif request.method == 'GET':
            print("No Post Back Call")
            Home_Item = {'Type': 'Home'}
            Home_Item_Dump = pickle.dumps(Home_Item)
            s.send(Home_Item_Dump)

            while True:
                home_data = s.recv(4096)
                if not home_data:
                    break

                global home_data_string
                home_data_string = pickle.loads(home_data)
                print('Receive_Home', repr(home_data_string))

                response = {'Type': "Response_Home", 'Data': 'Thank_You'}
                d_response = pickle.dumps(response)
                s.sendall(d_response)

                user_data_arr = session.get('user_data_arr')
                print("user_data_arr = ", user_data_arr)

                if user_data_arr is not None:
                    User_ID = user_data_arr[0][0]
                    First_Name = user_data_arr[0][1]
                    Last_Name = user_data_arr[0][2]

                    return render_template("home.html", data=home_data_string, User_ID=User_ID, user_data=user_data_arr, First_Name=First_Name, Last_Name=Last_Name)
                else:
                    return render_template("home.html", data=home_data_string,  user_data=user_data_arr)


    @app.route('/process', methods=['POST'])
    def process():
        global Broadcast_Data, Broadcast_Sub_Data
        #print("Broadcast_Data",Broadcast_Data)
        #print("Broadcast_Sub_Data", Broadcast_Sub_Data)

        name = request.form['name']
        #print("Request", name)
        if name == "Notification":
            Type_01 = Broadcast_Sub_Data["Type"]
            if Type_01 == "New_Bid":
                print("IN_New_BID", Broadcast_Sub_Data)
                Title = Broadcast_Sub_Data["Title"]
                Base_Price = Broadcast_Sub_Data["Base_Price"]
                Max_bid = Broadcast_Sub_Data["Max_bid"]
                return jsonify({'Type': "New_Bid", 'Title': Title, 'Base_Price': Base_Price, "Max_bid": Max_bid})

            Type_02 = Broadcast_Data["Type"]
            if Type_02 == "New_Item":
                Title = Broadcast_Data["Title"]
                Base_Price = Broadcast_Data["Base_Price"]
                Expiry_Date = Broadcast_Data["Expiry_Date"]
                return jsonify({'Type': "New_Item", 'Title': Title, 'Base_Price': Base_Price, "Expiry_Date": Expiry_Date})
            else:
                return jsonify({'error': 'Missing data!'})

        if name == "Notification_OFF":
            Broadcast_Data = {"Type": "No_New_Notification"}
            Broadcast_Sub_Data = {"Type": "No_New_Notification"}
            return jsonify({'error': 'Missing data!'})

    @app.route("/logout")
    def logout():
        user_data_arr = session.get('user_data_arr')
        User_ID = user_data_arr[0][0]

        Item_id = {'Type': 'Log_Out', 'User_ID': User_ID, 'multicast_IP': multicast_IP}
        Item_Dump = pickle.dumps(Item_id)
        s.send(Item_Dump)

        log_out_data = s.recv(1024)
        log_out_data_arr = pickle.loads(log_out_data)
        print('Received_Logout_Response', repr(log_out_data_arr))

        if log_out_data_arr["Data"] == "Log_out":
            session["user_data_arr"] = None

        else:
            print("Log_out_unsuccessful")
        flash("Logout successful")
        return redirect("/")


    @app.route("/nav")
    def nav():
        user_data_arr = session.get('user_data_arr')
        if user_data_arr is not None:
            First_Name = user_data_arr[0][1]
            Last_Name = user_data_arr[0][2]
            return render_template("layout.html", user_data=user_data_arr, First_Name=First_Name, Last_Name=Last_Name)
        else:
            return render_template("layout.html", user_data=user_data_arr)


    @app.route("/about")
    def about():
        user_data_arr = session.get('user_data_arr')
        if user_data_arr is not None:
            First_Name = user_data_arr[0][1]
            Last_Name = user_data_arr[0][2]
            return render_template("about.html", user_data=user_data_arr, First_Name=First_Name, Last_Name=Last_Name)
        else:
            return render_template("about.html", user_data=user_data_arr)


    @app.route("/item")
    def item():
        item_id = session.get('Item_ID')
        Item_Category = session.get('Item_Category')
        Item_id = {'Type': 'Item', 'Item_id': item_id, 'Item_Category': Item_Category}
        Item_Dump = pickle.dumps(Item_id)
        s.send(Item_Dump)

        while True:
            item_data = s.recv(4096)
            if not item_data:
                break

            global item_data_string
            item_data_arr = pickle.loads(item_data)
            print("item_data_arr", item_data_arr)
            item_data_string = item_data_arr["Item_Result"]
            item_max_bid_string = item_data_arr["Max_Bid_Result"]
            Related_Products_string = item_data_arr["Related_Products"]

            print('Receive_Item', repr(item_data_arr))

            response = {'Type': "Response_Home", 'Data': 'Thank_You'}
            d_response = pickle.dumps(response)
            s.sendall(d_response)

            Item_ID = item_data_string[0][0]
            Item_Owner_Id = item_data_string[0][1]
            Item_Image = item_data_string[0][2]
            Item_Title = item_data_string[0][3]
            Item_Category = item_data_string[0][4]
            Item_Base_Price = item_data_string[0][5]
            Item_Expiry_Date = item_data_string[0][6]
            Item_Main_Details = item_data_string[0][7]
            Item_Details = item_data_string[0][8]
            Item_Status = item_data_string[0][11]
            Time_Extended = item_data_string[0][12]
            Max_Bid = item_max_bid_string[0][0]

            user_data_arr = session.get('user_data_arr')

            if user_data_arr is not None:
                User_ID = user_data_arr[0][0]
                First_Name = user_data_arr[0][1]
                Last_Name = user_data_arr[0][2]
                return render_template("item.html", Item_ID=Item_ID, Item_Owner_Id=Item_Owner_Id,
                                       Item_Image=Item_Image, Item_Title=Item_Title, Item_Category=Item_Category,
                                       Item_Base_Price=Item_Base_Price, Item_Expiry_Date=Item_Expiry_Date, Item_Main_Details=Item_Main_Details,
                                       Item_Details=Item_Details, Item_Status=Item_Status, Time_Extended=Time_Extended, user_data=user_data_arr,
                                       User_ID=User_ID, First_Name=First_Name, Last_Name=Last_Name, Max_Bid=Max_Bid, Related_Products_string=Related_Products_string)
            else:
                return render_template("item.html", Item_ID=Item_ID, Item_Owner_Id=Item_Owner_Id,
                                       Item_Image=Item_Image, Item_Title=Item_Title, Item_Category=Item_Category,
                                       Item_Base_Price=Item_Base_Price, Item_Expiry_Date=Item_Expiry_Date,
                                       Item_Details=Item_Details, Item_Status=Item_Status, user_data=user_data_arr, Max_Bid=Max_Bid, Related_Products_string=Related_Products_string)


    @app.route("/dashboard", methods=['GET', 'POST'])
    def dashboard():
        print("Request_Method = ", request.method)
        if request.method == "GET":
            global Broadcast_Data, dashboard_own_items, dashboard_bid_items, user_acc
            global Broadcast_Sub_Data

            user_data_arr = session.get('user_data_arr')
            User_Id = user_data_arr[0][0]

            dashboard_Item = {'Type': 'Dashboard', 'User_ID': User_Id}
            dashboard_Bid_Item_Dump = pickle.dumps(dashboard_Item)
            s.send(dashboard_Bid_Item_Dump)

            while True:
                dashboard_Item = s.recv(4096)
                if not dashboard_Item:
                    break
                print(dashboard_Item)
                dashboard_Item_string = pickle.loads(dashboard_Item)
                user_acc = dashboard_Item_string["User_Acc"]
                session['user_data_arr'] = user_acc
                dashboard_bid_items = dashboard_Item_string["Bid_Items"]
                dashboard_own_items = dashboard_Item_string["Own_Items"]
                dashboard_win_bids = dashboard_Item_string["Win_Bid"]
                dashboard_sub_items = dashboard_Item_string["Sub_Items"]
                #print(dashboard_Item_string)

                User_ID = user_acc[0][0]
                First_Name = user_acc[0][1]
                Last_Name = user_acc[0][2]
                Mobile_Number = user_acc[0][3]
                Email = user_acc[0][4]
                Address = user_acc[0][5]
                print("ado Why Bng?")
                return render_template("dashboard.html", User_Id=User_Id, First_Name=First_Name, Last_Name=Last_Name,
                                       Mobile_Number=Mobile_Number, Email=Email, Address=Address,
                                       dashboard_bid_items=dashboard_bid_items, dashboard_own_items=dashboard_own_items, dashboard_win_bids=dashboard_win_bids,dashboard_sub_items=dashboard_sub_items)

    @app.route("/edit_profile", methods=['GET', 'POST'])
    def edit_profile():
        print("Request_Method = ", request.method)
        if request.method == "POST":
            if request.form.get("Save_Changes") == "Save_Changes":
                First_Name = request.form.get("First_Name")
                Last_Name = request.form.get('Last_Name')
                Email = request.form.get('Email')
                Phone_Number = request.form.get('Phone_Number')
                Address = request.form.get('Address')

                print(First_Name, Last_Name, Email, Phone_Number, Address)

                user_acc_arr = session.get('user_data_arr')
                User_Id = user_acc_arr[0][0]

                user_acc_edit = {'Type': 'Edit_User_Acc', "User_Id": User_Id, 'First_Name': First_Name, 'Last_Name': Last_Name, 'Phone_Number': Phone_Number, 'Email': Email, 'Address': Address}
                user_acc_edit_arr = pickle.dumps(user_acc_edit)
                s.send(user_acc_edit_arr)

                edit_profile_data = s.recv(4096)
                edit_profile_arr = pickle.loads(edit_profile_data)
                print('Response = ', repr(edit_profile_arr))
                flash("User account update successful")
                return redirect('dashboard')


    @app.route("/supplier", methods=['GET', 'POST'])
    def supplier():
        print("Request_Method = ", request.method)
        if request.method == "POST":
            if request.form.get("New_Item") == "New_Item":
                Owner_ID = request.form.get("User_ID")
                Image = request.form.get('Image')
                Title = request.form.get('Title')
                Category = request.form.get('Category')
                Base_Price = request.form.get('Base_Price')
                Special_Time = request.form.get("Special_Time")
                if Special_Time == "True":
                    Expiry_Date = request.form.get("Time")
                    Sub_Type = "Special"
                else:
                    Expiry_Date = request.form.get('Expiry_Date')
                    Sub_Type = "Normal"
                Main_Details = request.form.get('Main_Details')
                Details = request.form.get('Details')

                print(Owner_ID, Image, Title, Category, Base_Price, Special_Time, Expiry_Date, Details)

                new_item = {"Type": "New_Item", "Sub_Type": Sub_Type, "Owner_ID": Owner_ID, "Image": Image, "Title": Title, "Category": Category,
                            "Base_Price": Base_Price, "Expiry_Date": Expiry_Date, "Main_Details": Main_Details, "Details": Details}

                new_item_arr = pickle.dumps(new_item)
                s.send(new_item_arr)

                data = s.recv(4096)
                data_arr = pickle.loads(data)
                print('Received_Response', repr(data_arr))
                flash("Add item successful")

        user_data_arr = session.get('user_data_arr')
        if user_data_arr is not None:
            User_ID = user_data_arr[0][0]
            First_Name = user_data_arr[0][1]
            Last_Name = user_data_arr[0][2]
            return redirect("dashboard")
        else:
            return redirect('/')

    if __name__ == "__main__":
        app.run(debug=True, host="127.0.0.5", port=1235)
