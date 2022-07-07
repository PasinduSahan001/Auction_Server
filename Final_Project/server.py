import socket
import pickle
import mysql.connector
import datetime
import threading
import schedule
import time
from datetime import datetime
import pandas

data_base = mysql.connector.connect(
    host='127.0.0.3',
    user='root',
    passwd='root',
    database='cmp_mini'
)

db_01 = data_base.cursor()

HOST = '127.0.0.1'
PORT = 2021
Thread_Count = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as error:
    print(str(error))

print('© 2022 Pasindu Sahan Rathnayaka')
s.listen()

multicast_connections = []
global dashboard_arr


def thread_client(conn):
    conn.send(str.encode("Welcome to the Real Estate Auction System Created by Pasindu Sahan Rathnayaka"))

    while True:
        data = conn.recv(4096)
        if not data:
            break

        data_string = pickle.loads(data)
        print('Received', repr(data_string))
        # conn.sendall(data)

        Type = data_string["Type"]
        print('Type = ', Type)

        if Type == "Log_In":
            # response = {'Type': "Response", 'Data': 'Thank_You'}
            # d_response = pickle.dumps(response)
            # conn.sendall(d_response)

            email = data_string["email"]
            password = data_string["password"]
            print(email, password)

            login_sql = """SELECT COUNT(email) FROM user WHERE email ='%s' AND password = '%s' """ % (email, password)
            db_01.execute(login_sql)
            login_result = db_01.fetchall()
            print("Log count", login_result[0][0])
            if login_result[0][0] == 1:
                log_in_sql = """SELECT user_id, First_Name, Last_Name, Phone_Number, Email, Address FROM user WHERE email ='%s' AND password = '%s' """ % (email, password)
                db_01.execute(log_in_sql)
                user_result = db_01.fetchall()
                print("user_details", user_result)
                user_arr = {"Type": "User", "Data": user_result}
                user_details = pickle.dumps(user_arr)
                conn.sendall(user_details)

            elif login_result[0][0] != 1:
                email_checking_sql = """SELECT COUNT(email) FROM user WHERE email = '%s' """ % email
                db_01.execute(email_checking_sql)
                email_checking = db_01.fetchall()
                if email_checking[0][0] == 1:
                    response = {'Type': "Error", 'Data': 'Please check your password and try again'}
                    user_acc_response = pickle.dumps(response)
                    conn.sendall(user_acc_response)

                if email_checking[0][0] != 1:
                    response = {'Type': "Error", 'Data': 'Please check your email and try again'}
                    user_acc_response = pickle.dumps(response)
                    conn.sendall(user_acc_response)

            else:
                response = {'Type': "Error", 'Data': 'Unexpected error occurred'}
                d_response = pickle.dumps(response)
                conn.sendall(d_response)

        if Type == "Sign_Up":
            #response = {'Type': "Response", 'Data': 'Thank_You'}
            #d_response = pickle.dumps(response)
            #conn.sendall(d_response)

            print('ON')
            First_Name = data_string["First_Name"]
            Last_Name = data_string["Last_Name"]
            Phone_Number = data_string["Phone_Number"]
            Email = data_string["Email"]
            Password = data_string["Password"]

            print(First_Name, Last_Name, Phone_Number, Email, Password)

            email_checking_sql = """SELECT COUNT(email) FROM user WHERE email = '%s' """ % Email
            db_01.execute(email_checking_sql)
            email_checking = db_01.fetchall()

            mobile_checking_sql = """SELECT COUNT(email) FROM user WHERE Phone_Number ='%s' """ % Phone_Number
            db_01.execute(mobile_checking_sql)
            mobile_checking = db_01.fetchall()

            if email_checking[0][0] != 1 and mobile_checking[0][0] != 1:
                try:
                    sql = "INSERT INTO user (user_id, First_Name, Last_Name, Phone_Number, Email, Password) VALUES (NULL, %s, %s, %s,  %s, %s);"
                    val = (First_Name, Last_Name, Phone_Number, Email, Password)
                    db_01.execute(sql, val)
                    data_base.commit()

                    user_id_find_sql = "SELECT user_id FROM user WHERE Phone_Number = %s;" % Phone_Number
                    db_01.execute(user_id_find_sql)
                    user_id_arr = db_01.fetchall()
                    print("Sign_Up_User_ID: ", user_id_arr)
                    user_id = user_id_arr[0][0]

                    multicast_sql = "INSERT INTO multicast VALUES (Null, %s, NULL);" % user_id
                    db_01.execute(multicast_sql)
                    data_base.commit()

                    response = {'Type': "Response", 'Data': 'User Create successfully '}
                    user_acc_response = pickle.dumps(response)
                    conn.sendall(user_acc_response)

                except:
                    response = {'Type': "Response", 'Data': 'Unexpected error occurred'}
                    user_acc_response = pickle.dumps(response)
                    conn.sendall(user_acc_response)

            if email_checking[0][0] == 1 and mobile_checking[0][0] != 1:
                response = {'Type': "Response", 'Data': 'This email is taken by another user'}
                user_acc_response = pickle.dumps(response)
                conn.sendall(user_acc_response)

            if mobile_checking[0][0] == 1 and email_checking[0][0] != 1:
                response = {'Type': "Response", 'Data': 'This mobile number is taken by another user'}
                user_acc_response = pickle.dumps(response)
                conn.sendall(user_acc_response)

            if email_checking[0][0] == 1 and mobile_checking[0][0] == 1:
                response = {'Type': "Response", 'Data': 'This email and mobile number is taken by another user'}
                user_acc_response = pickle.dumps(response)
                conn.sendall(user_acc_response)

        if Type == "Home":
            home_sql = """SELECT item_id, item_image_link, item_title, item_category, item_status ,item_base_price, item_expiry_date, item_main_details FROM cmp_mini.items;"""
            db_01.execute(home_sql)
            home_result = db_01.fetchall()
            # Home_item = {'Type': 'Home'}
            print(home_result)
            Home_arr = pickle.dumps(home_result)
            conn.sendall(Home_arr)

        #if Type == "Response_Home":
            #conn.close()

        if Type == "Item":
            item_id = data_string["Item_id"][0]
            item_category = data_string["Item_Category"][0]

            item_sql = """SELECT * FROM items WHERE item_id = %s; """ % item_id
            db_01.execute(item_sql)
            item_result = db_01.fetchall()
            print(item_result)

            max_bid_sql = "SELECT max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
            db_01.execute(max_bid_sql)
            max_bid_result = db_01.fetchall()
            print(max_bid_result)

            related_products_sql = "SELECT item_id, item_image_link, item_title, item_base_price, item_category FROM items WHERE item_category= '%s' AND item_status= 'Available' AND item_id <> %s LIMIT 4;" % (item_category, item_id)
            db_01.execute(related_products_sql)
            related_products_result = db_01.fetchall()
            print(related_products_result)

            item_data = {"Item_Result": item_result, "Max_Bid_Result": max_bid_result, "Related_Products": related_products_result}
            Item_arr = pickle.dumps(item_data)
            conn.sendall(Item_arr)

        if Type == "Dashboard":
            User_ID = data_string["User_ID"]
            print("User_Id= ", User_ID)

            user_acc_sql = """SELECT user_id, First_Name, Last_Name, Phone_Number, Email, Address FROM user WHERE user_id = '%s' """ % User_ID
            db_01.execute(user_acc_sql)
            user_acc_result = db_01.fetchall()
            print("user_acc_details", user_acc_result)

            dashboard_bid_sql = "SELECT item_title,item_base_price, bid_price FROM items LEFT JOIN bid_item ON bid_item.bid_item_id = items.item_id LEFT JOIN user ON bid_item.bid_buyer_id = user.user_id WHERE user_id = %s and bid_item.bid_price <> 'NULL';" % User_ID
            db_01.execute(dashboard_bid_sql)
            dashboard_bid_result = db_01.fetchall()
            print(dashboard_bid_result)

            dashboard_sub_sql = "SELECT DISTINCT item_id,item_title,item_base_price, bid_status FROM items LEFT JOIN bid_item ON bid_item.bid_item_id = items.item_id LEFT JOIN user ON bid_item.bid_buyer_id = user.user_id WHERE user_id = %s and bid_item.bid_status = 'SUB';" % User_ID
            db_01.execute(dashboard_sub_sql)
            dashboard_sub_result = db_01.fetchall()
            print("dashboard_sub_result: ", dashboard_sub_result)

            dashboard_win_bid_sql = "SELECT item_title, item_base_price, item_sold_price FROM items WHERE item_buyer = %s;" % User_ID
            db_01.execute(dashboard_win_bid_sql)
            dashboard_win_bid_result = db_01.fetchall()
            print(dashboard_win_bid_result)

            dashboard_own_items_sql = "SELECT DISTINCT item_id, item_title,item_base_price, item_status FROM items LEFT JOIN bid_item ON bid_item.bid_item_id = items.item_id WHERE item_owner_id = %s;" % User_ID
            db_01.execute(dashboard_own_items_sql)
            dashboard_own_items_result = db_01.fetchall()
            print("dashboard_own_items_result: ", dashboard_own_items_result)

            own_item_id = []
            for i in dashboard_own_items_result:
                own_item_id.append(i[0])

            own_items_with_max = []
            c = []
            for m in range(0, len(own_item_id)):
                own_items_max_sql = "SELECT max(bid_price) FROM bid_item WHERE bid_item_id = %s" % own_item_id[m]
                db_01.execute(own_items_max_sql)
                dashboard_own_items_max_result = db_01.fetchall()
                #print(dashboard_own_items_max_result)

                temp_id = dashboard_own_items_result[m][0]
                temp_title = dashboard_own_items_result[m][1]
                temp_base_price = dashboard_own_items_result[m][2]
                temp_item_status = dashboard_own_items_result[m][3]
                temp_max = dashboard_own_items_max_result[0]
                re_create = (temp_id, temp_title, temp_base_price, temp_max, temp_item_status)
                own_items_with_max.append(re_create)

            dashboard_result = {"User_Acc": user_acc_result, "Bid_Items": dashboard_bid_result, "Own_Items": own_items_with_max, "Win_Bid": dashboard_win_bid_result, "Sub_Items": dashboard_sub_result}
            global dashboard_arr
            dashboard_arr = pickle.dumps(dashboard_result)
            conn.sendall(dashboard_arr)

        if Type == "Bid":

            User_ID = data_string["User_ID"]
            Item_ID = data_string["Item_ID"]
            Time_Extended = data_string["Time_Extended"]
            Expiry_Date = data_string["Expiry_Date"]
            Bid_Price = data_string["Bid_Price"]

            if bid_end_check(Expiry_Date) > 60 or Time_Extended == "TRUE":
                print("bid_end_check: ", bid_end_check(Expiry_Date))
                print("User_Id= ", User_ID, "Item_ID= ", Item_ID, "Bid_Price= ", Bid_Price)
                bid_sql = "INSERT INTO bid_item (bid_id, bid_item_id, bid_buyer_id, bid_price, bid_status) VALUES (NULL, %s, %s, %s,  NULL);"
                val = (Item_ID, User_ID, Bid_Price)
                db_01.execute(bid_sql, val)
                data_base.commit()

                response = {'Type': "Response", 'Data': 'Updated'}
                bid_response = pickle.dumps(response)
                conn.sendall(bid_response)

                bid_notification_sql = "SELECT item_title, item_base_price, max(bid_price) FROM items LEFT JOIN bid_item ON items.item_id = bid_item.bid_item_id WHERE item_id = %s;" % Item_ID
                db_01.execute(bid_notification_sql)
                bid_notification_arr = db_01.fetchall()
                print(bid_notification_arr)

                Title = bid_notification_arr[0][0]
                Base_Price = bid_notification_arr[0][1]
                Max_bid = bid_notification_arr[0][2]

                new_bid_arr = {"Type": "New_Bid", "Item_ID": Item_ID, "Title": Title, "Base_Price": Base_Price, "Max_bid": Max_bid}
                Notification_Type = "New_Bid"
                mu = threading.Thread(target=new_item_notification, args=(Notification_Type, new_bid_arr))
                mu.start()

            if bid_end_check(Expiry_Date) <= 60 and Time_Extended != "TRUE":

                response = {'Type': "Response", 'Data': 'Time_Extended'}
                bid_response = pickle.dumps(response)
                conn.sendall(bid_response)

                current_time = str(datetime.now())
                current_time_expand = current_time[:19]
                date_format_str = '%Y-%m-%d %H:%M:%S'
                time_convert = datetime.strptime(current_time_expand, date_format_str)
                print("time_convert", time_convert)
                extended_time = 60+bid_end_check(Expiry_Date)
                final_time = time_convert + pandas.DateOffset(seconds=extended_time)
                final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
                print("final_time_str", final_time_str)

                bid_sql = "INSERT INTO bid_item (bid_id, bid_item_id, bid_buyer_id, bid_price, bid_status) VALUES (NULL, %s, %s, %s,  NULL);"
                val = (Item_ID, User_ID, Bid_Price)
                db_01.execute(bid_sql, val)
                data_base.commit()

                datetime_sql = "UPDATE items SET item_expiry_date = %s, time_extended = 'TRUE' WHERE item_id = %s;"
                val = (final_time_str, Item_ID,)
                db_01.execute(datetime_sql, val)
                data_base.commit()

                bid_notification_sql = "SELECT item_title, item_base_price, max(bid_price) FROM items LEFT JOIN bid_item ON items.item_id = bid_item.bid_item_id WHERE item_id = %s;" % Item_ID
                db_01.execute(bid_notification_sql)
                bid_notification_arr = db_01.fetchall()
                print(bid_notification_arr)

                Title = bid_notification_arr[0][0]
                Base_Price = bid_notification_arr[0][1]
                Max_bid = bid_notification_arr[0][2]

                new_bid_arr = {"Type": "New_Bid", "Item_ID": Item_ID, "Title": Title, "Base_Price": Base_Price,
                               "Max_bid": Max_bid}
                Notification_Type = "New_Bid"
                mu = threading.Thread(target=new_item_notification, args=(Notification_Type, new_bid_arr))
                mu.start()

                time.sleep(0.5)

        if Type == "Item_Sub":
            User_ID = data_string["User_ID"]
            Item_ID = data_string["Item_ID"]
            # Time_Extended = data_string["Time_Extended"]
            # Expiry_Date = data_string["Expiry_Date"]
            # Bid_Price = data_string["Bid_Price"]

            try:
                item_sub_sql = "INSERT INTO bid_item (bid_id, bid_item_id, bid_buyer_id, bid_price, bid_status) VALUES (NULL, %s, %s, NULL, 'SUB');"
                val = (Item_ID, User_ID)
                db_01.execute(item_sub_sql, val)
                data_base.commit()

                response = {'Type': "Response", 'Data': 'From here you will receive notifications about this item.'}
                bid_response = pickle.dumps(response)
                conn.sendall(bid_response)
            except:
                response = {'Type': "Response", 'Data': 'Subscribe Error'}
                bid_response = pickle.dumps(response)
                conn.sendall(bid_response)

        if Type == "New_Item":
            Sub_Type = data_string["Sub_Type"]
            Owner_ID = data_string["Owner_ID"]
            Image = data_string["Image"]
            Title = data_string["Title"]
            Category = data_string["Category"]
            Base_Price = data_string["Base_Price"]
            Expiry_Date = data_string["Expiry_Date"]
            Main_Details = data_string["Main_Details"]
            Details = data_string["Details"]

            print(Image, Title, Category, Base_Price, Expiry_Date, Details, Sub_Type)

            if Sub_Type == "Normal":
                new_item_sql = "INSERT INTO items (item_id, item_owner_id, item_image_link, item_title, item_category, item_base_price, item_expiry_date, item_main_details, item_details, item_status, time_extended, priority) VALUES (NULL, %s, %s, %s, %s,%s, %s, %s, %s, 'Available', 'FALSE', 'Normal');"
                val = (Owner_ID, Image, Title, Category, Base_Price, Expiry_Date, Main_Details, Details)
                db_01.execute(new_item_sql, val)
                data_base.commit()

                response = {'Type': "Response", 'Data': 'Updated'}
                new_item_response = pickle.dumps(response)
                conn.sendall(new_item_response)

                new_item_arr = {"Type": "New_Item", "Image": Image, "Title": Title, "Base_Price": Base_Price, "Expiry_Date": Expiry_Date}
                Notification_Type = "New_Item"
                mu = threading.Thread(target=new_item_notification, args=(Notification_Type, new_item_arr))
                mu.start()

            if Sub_Type == "Special":
                Expiry_Date_raw = data_string["Expiry_Date"]
                Expiry_Date = int(Expiry_Date_raw)

                current_time = str(datetime.now())
                current_time_expand = current_time[:19]
                date_format_str = '%Y-%m-%d %H:%M:%S'
                time_convert = datetime.strptime(current_time_expand, date_format_str)
                print("time_convert", time_convert)
                extended_time = Expiry_Date
                final_time = time_convert + pandas.DateOffset(hours=extended_time)
                final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
                print("final_time_str", final_time_str)

                Notification_Time = f"{Expiry_Date_raw} Hours "

                new_item_sql = "INSERT INTO items (item_id, item_owner_id, item_image_link, item_title, item_category, item_base_price, item_expiry_date, item_main_details, item_details, item_status, time_extended, priority) VALUES (NULL, %s, %s, %s, %s,%s, %s, %s, %s, 'Available', 'FALSE', 'Special' );"
                val = (Owner_ID, Image, Title, Category, Base_Price, final_time_str, Main_Details, Details)
                db_01.execute(new_item_sql, val)
                data_base.commit()

                response = {'Type': "Response", 'Data': 'Updated'}
                new_item_response = pickle.dumps(response)
                conn.sendall(new_item_response)

                new_item_arr = {"Type": "New_Item", "Image": Image, "Title": Title, "Base_Price": Base_Price,
                                "Expiry_Date": Notification_Time}
                Notification_Type = "New_Item"
                mu = threading.Thread(target=new_item_notification, args=(Notification_Type, new_item_arr))
                mu.start()

        if Type == "Multicasting_Request":
            Multicasting_ID = data_string["Multicasting_ID"]
            User_ID = data_string["User_ID"]
            print("Multicasting_ID: ", Multicasting_ID)
            if Multicasting_ID not in multicast_connections:
                multicast_connections.append(Multicasting_ID)

                multicast_sql = "UPDATE multicast SET broadcast_IP= %s WHERE user_id = %s;"
                val = (Multicasting_ID, User_ID,)
                db_01.execute(multicast_sql, val)
                data_base.commit()

        if Type == "Log_Out":
            User_ID = data_string["User_ID"]
            multicast_IP = data_string["multicast_IP"]
            print("Before = ", multicast_connections)
            if multicast_IP in multicast_connections:
                multicast_connections.remove(multicast_IP)
            print("After = ", multicast_connections)
            log_out_sql = "UPDATE multicast SET broadcast_IP= NULL WHERE user_id = '%s';" % User_ID
            db_01.execute(log_out_sql)
            data_base.commit()

            response = {'Type': "Response", 'Data': 'Log_out'}
            log_out_response = pickle.dumps(response)
            conn.sendall(log_out_response)

        if Type == "Edit_User_Acc":
            response = {'Type': "Response", 'Data': 'Thank_You'}
            d_response = pickle.dumps(response)
            conn.sendall(d_response)

            User_Id = data_string["User_Id"]
            First_Name = data_string["First_Name"]
            Last_Name = data_string["Last_Name"]
            #Phone_Number = data_string["Phone_Number"]
            #Email = data_string["Email"]
            Address = data_string["Address"]

            print(First_Name, Last_Name, Address)

            sql = "UPDATE user SET First_Name = %s, Last_Name = %s, Address = %s  WHERE user_id = %s;"
            val = (First_Name, Last_Name, Address, User_Id)
            db_01.execute(sql, val)
            data_base.commit()


def bid_end_check(Expiry_Date):
    while True:
        time_str = Expiry_Date
        date_format_str = '%Y-%m-%d %H:%M:%S'
        expiry_time = datetime.strptime(time_str, date_format_str)
        now = datetime.now()
        duration = expiry_time - now
        duration_in_s = duration.total_seconds()
        print("bid_end_check", duration_in_s)

        return duration_in_s


def bid_end():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended <> 'TRUE' AND item_status = "Available" AND priority = "Normal" ;"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    #print(home_result)
    bid_ended_items = []
    while True:
        for i in range(0, len(item_result)):
            arr = str(item_result[i][1])
            date_format_str = '%Y-%m-%d %H:%M:%S'
            expiry_time = datetime.strptime(arr, date_format_str)
            now_01 = str(datetime.now())
            now_02 = (now_01[:19])
            ex = datetime.strptime(now_02, date_format_str)
            duration = expiry_time - ex
            duration_in_s = duration.total_seconds()
            #print("Final", duration_in_s)

            if duration_in_s < 2:
                item_id = item_result[i][0]
                max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
                db_01.execute(max_bid_sql)
                max_bid_result = db_01.fetchall()
                bid_ended_items.append(max_bid_result)

        #print(bid_ended_items)
        for update_item in bid_ended_items:
            #print(update_item)
            bid_item_id = update_item[0][0]
            bid_buyer_id = update_item[0][1]
            sold_price = update_item[0][2]
            #print(bid_item_id,bid_buyer_id,sold_price)

            final_bid_sql = "UPDATE items SET item_buyer = %s, item_sold_price = %s, item_status='Sold' WHERE item_id = %s;"
            val = (bid_buyer_id, sold_price, bid_item_id)
            db_01.execute(final_bid_sql, val)
            data_base.commit()
        print("Final_Bid_Updated")
        break
    print("end")


def extended_bid_end():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended = 'TRUE' AND item_status = "Available" AND priority = "Normal";"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    #print(home_result)
    bid_ended_items = []

    while True:
        for i in range(0, len(item_result)):
            item_id = item_result[i][0]
            max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
            db_01.execute(max_bid_sql)
            max_bid_result = db_01.fetchall()
            bid_ended_items.append(max_bid_result)

        #print(bid_ended_items)
        for update_item in bid_ended_items:
            #print(update_item)
            bid_item_id = update_item[0][0]
            bid_buyer_id = update_item[0][1]
            sold_price = update_item[0][2]
            #print(bid_item_id,bid_buyer_id,sold_price)

            final_bid_sql = "UPDATE items SET item_buyer = %s, item_sold_price = %s, item_status='Sold' WHERE item_id = %s;"
            val = (bid_buyer_id, sold_price, bid_item_id)
            db_01.execute(final_bid_sql, val)
            data_base.commit()
        print("Final_Bid_Updated")
        break
    print("end")


def force_end_bid():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended <> 'TRUE' AND item_status = "Available" AND priority = "Normal";"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    bid_ended_items = []
    while True:
        for i in range(0, len(item_result)):
            arr = str(item_result[i][1])
            date_format_str = '%Y-%m-%d %H:%M:%S'
            expiry_time = datetime.strptime(arr, date_format_str)
            now_01 = str(datetime.now())
            now_02 = (now_01[:19])
            ex = datetime.strptime(now_02, date_format_str)
            duration = expiry_time - ex
            duration_in_s = duration.total_seconds()

            if duration_in_s < 0:
                item_id = item_result[i][0]
                force_end_bid_sql = "UPDATE items SET item_status='Expired' WHERE item_id = %s;" % item_id
                db_01.execute(force_end_bid_sql)
                data_base.commit()
        print("force_end_bid")
        break
    print("end")


def end_special_bid():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended <> 'TRUE' AND item_status = "Available" AND priority = "Special" ;"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    # print(home_result)
    bid_ended_items = []
    while True:
        for i in range(0, len(item_result)):
            arr = str(item_result[i][1])
            date_format_str = '%Y-%m-%d %H:%M:%S'
            expiry_time = datetime.strptime(arr, date_format_str)
            now_01 = str(datetime.now())
            now_02 = (now_01[:19])
            ex = datetime.strptime(now_02, date_format_str)
            duration = expiry_time - ex
            global duration_in_s
            duration_in_s = duration.total_seconds()
            # print("Final", duration_in_s)

            if duration_in_s < 60:
                item_id = item_result[i][0]
                max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
                db_01.execute(max_bid_sql)
                max_bid_result = db_01.fetchall()
                bid_ended_items.append(max_bid_result)

        # print(bid_ended_items)
        for r in range(0, len(bid_ended_items)):
            # print(update_item)
            bid_item_id = bid_ended_items[r][0][0]
            bid_buyer_id = bid_ended_items[r][0][1]
            sold_price = bid_ended_items[r][0][2]
            # print(bid_item_id,bid_buyer_id,sold_price)

            final_bid_sql = "UPDATE items SET item_buyer = %s, item_sold_price = %s, item_status='Sold' WHERE item_id = %s;"
            val = (bid_buyer_id, sold_price, bid_item_id)
            db_01.execute(final_bid_sql, val)
            data_base.commit()
            if r <= (len(bid_ended_items)-1):
                print("Final_Bid_Updated")
                current_time = str(datetime.now())
                current_time_expand = current_time[:19]
                date_format_str = '%Y-%m-%d %H:%M:%S'
                time_convert = datetime.strptime(current_time_expand, date_format_str)
                print("time_convert", time_convert)
                extended_time = 60 + duration_in_s
                final_time = time_convert + pandas.DateOffset(seconds=extended_time)
                final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
                print("final_time_str", final_time_str)
                ex_run_time = str(final_time_str[11:])
                schedule.every().day.at(ex_run_time).do(end_special_extended_bid)
                force_end_special_bid()
        break
    print("end")


def force_end_special_bid():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended <> 'TRUE' AND item_status = "Available" AND priority = "Special";"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    bid_ended_items = []
    while True:
        for i in range(0, len(item_result)):
            arr = str(item_result[i][1])
            date_format_str = '%Y-%m-%d %H:%M:%S'
            expiry_time = datetime.strptime(arr, date_format_str)
            now_01 = str(datetime.now())
            now_02 = (now_01[:19])
            ex = datetime.strptime(now_02, date_format_str)
            duration = expiry_time - ex
            duration_in_s = duration.total_seconds()

            if duration_in_s < 0:
                item_id = item_result[i][0]
                force_end_bid_sql = "UPDATE items SET item_status='Expired' WHERE item_id = %s;" % item_id
                db_01.execute(force_end_bid_sql)
                data_base.commit()
        print("force_end_special_bid")
        break
    print("end")


def end_special_extended_bid():
    item_sql = """SELECT item_id, item_expiry_date FROM items WHERE time_extended = 'TRUE' AND item_status = "Available" AND priority = "Special" ;"""
    db_01.execute(item_sql)
    item_result = db_01.fetchall()
    # print(home_result)
    bid_ended_items = []
    while True:
        for i in range(0, len(item_result)):
            arr = str(item_result[i][1])
            date_format_str = '%Y-%m-%d %H:%M:%S'
            expiry_time = datetime.strptime(arr, date_format_str)
            now_01 = str(datetime.now())
            now_02 = (now_01[:19])
            ex = datetime.strptime(now_02, date_format_str)
            duration = expiry_time - ex
            duration_in_s = duration.total_seconds()
            # print("Final", duration_in_s)

            if duration_in_s < 5:
                item_id = item_result[i][0]
                max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
                db_01.execute(max_bid_sql)
                max_bid_result = db_01.fetchall()
                bid_ended_items.append(max_bid_result)

        # print(bid_ended_items)
        for update_item in bid_ended_items:
            # print(update_item)
            bid_item_id = update_item[0][0]
            bid_buyer_id = update_item[0][1]
            sold_price = update_item[0][2]
            # print(bid_item_id,bid_buyer_id,sold_price)

            final_bid_sql = "UPDATE items SET item_buyer = %s, item_sold_price = %s, item_status='Sold' WHERE item_id = %s;"
            val = (bid_buyer_id, sold_price, bid_item_id)
            db_01.execute(final_bid_sql, val)
            data_base.commit()
        print("Final_Bid_Updated")
        break
    print("end")


def new_item_notification(Notification_Type, Data):
    #print("New_Item_Func")
    #print("Data: ", Data)
    new_item_arr = Data
    if Notification_Type == "New_Item":
        all_user_sql = "SELECT broadcast_IP FROM multicast WHERE broadcast_IP IS NOT NULL;"
        db_01.execute(all_user_sql)
        all_users = db_01.fetchall()
        print("all_user= ", all_users)

        for m_ip in range(0, len(all_users)):
            MCAST_GRP = all_users[m_ip][0]
            MCAST_PORT = 2022
            MULTICAST_TTL = 10
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
            multicasting_response = {'Type': 'Broadcast', 'Response': new_item_arr}
            multicasting_response_Dump = pickle.dumps(multicasting_response)
            sock.sendto(multicasting_response_Dump, (MCAST_GRP, MCAST_PORT))
            if m_ip == (len(multicast_connections)-1):
                m_ip = 0
                break

    if Notification_Type == "New_Bid":
        new_bid_arr = Data
        Item_ID = new_bid_arr["Item_ID"]
        sub_user_sql = "SELECT DISTINCT bid_buyer_id FROM bid_item WHERE bid_item_id = %s;" % Item_ID
        db_01.execute(sub_user_sql)
        sub_user = db_01.fetchall()
        print("sub_user", sub_user)

        sub_user_arr = []
        for i in sub_user:
            print("sub_user", i[0])
            sub_user_arr.append(i[0])

        broadcast_ip_arr = []
        for i in sub_user_arr:
            sub_user_broadcast_IP_sql = "SELECT broadcast_IP FROM multicast WHERE user_id = %s;" % i
            db_01.execute(sub_user_broadcast_IP_sql)
            broadcast_IP = db_01.fetchall()
            print("broadcast_IP[0][0]", broadcast_IP[0][0])

            if broadcast_IP[0][0] is None:
                pass

            if broadcast_IP[0][0] is not None:
                print("None")
                broadcast_ip_arr.append(broadcast_IP[0][0])

        print("broadcast_ip_arr: ", broadcast_ip_arr)
        for m_ip in range(0, len(broadcast_ip_arr)):
            print("New_Bid_Func_loop")
            MCAST_GRP = broadcast_ip_arr[m_ip]
            MCAST_PORT = 2022
            MULTICAST_TTL = 10
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

            multicasting_response = {'Type': 'Broadcast_Sub', 'Response': new_bid_arr}
            multicasting_response_Dump = pickle.dumps(multicasting_response)
            sock.sendto(multicasting_response_Dump, (MCAST_GRP, MCAST_PORT))
            if m_ip == (len(multicast_connections)-1):
                sub_user_arr = []
                break


def test():
    print("LOL")


#esb = threading.Thread(target=end_special_bid)
#esb.start()
schedule.every(1).minutes.do(end_special_bid)
schedule.every().day.at("23:59:57").do(bid_end)
schedule.every().day.at("00:00:01").do(force_end_bid)
schedule.every().day.at("00:01:02").do(extended_bid_end)


def clock():
    while True:
        schedule.run_pending()
        time.sleep(0.5)


tik_tik = threading.Thread(target=clock)
tik_tik.start()


while True:
    client, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    cl = threading.Thread(target=thread_client, args=(client,))
    cl.start()
    Thread_Count += 1
    print('Thread Number: ' + str(Thread_Count))
    print(multicast_connections)
