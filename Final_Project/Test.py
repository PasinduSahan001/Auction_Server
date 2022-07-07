#x = [(0, 'Note 20 ultra', '12GB Ram', 235000, None, None, 'Available', None, None, None), (1, 'Apple 13', 'Ane manda', 200000, None, None, 'Available', None, None, None)]
#
#
##i = 0
##for i in range(0, len(x)):
##    print(x[i])
#
#for item in x:
#    print(item[1])
#
#print(len(x))

import datetime
import pickle



#def index():
#    local_list = 'Note 20 ultra'
#    return local_list
#
#def item(passed_list):
#    print(passed_list)
#
#def data_transfer():
#    # returned list is ignored
#    returned_list = index()
#
#    # passed_list inside useTheList is set to what is returned from defineAList
#    item(returned_list)
#
#data_transfer()
#
#user = [(1, 'Pasindu', 'Sahan', '0774515356', 'pasindusahan001@gmail.com', '1234')]
#arr = {"Type":"Login", "Data": user}
#
#print(arr)
#
#
#item_data_string = [(1, 1, 'static\\image\\note_20 ultra.png', 'Note 20 ultra', 'Phone', 235000.0, None, '12GB RAM', None, None, 'ACTIVE', None)]
#
#Item_ID = item_data_string[0][0]
#Item_Owner_Id = item_data_string[0][1]
#Item_Image = item_data_string[0][1]
#Item_Title = item_data_string[0][3]
#Item_Category = item_data_string[0][4]
#Item_Base_Price = item_data_string[0][5]
#Item_Expiry_Date = item_data_string[0][6]
#Item_Details = item_data_string[0][7]
#Item_Status = item_data_string[0][8]
#
#Home_Item_ID = item_data_string[0][0]
#Home_Item_Image = item_data_string[0][1]
#Home_Item_Title = item_data_string[0][3]
#Home_Item_Category = item_data_string[0][4]
#Home_Item_Status = item_data_string[0][8]
#
#date = "2021-12-02 00:00:00"
#
#time_format = date.replace(":", ",")
#print(time_format)
#date_format = time_format.replace("-", ",")
#print(date_format)
#final_raw_format = date_format.replace(" ", ",")
#print(final_raw_format)
#
#final_format = final_raw_format.rsplit(',')
#print(final_format[4])
#
#year = int(final_format[0])
#month = int(final_format[1])
#day = int(final_format[2])
#
#hours = int(final_format[3])
#minutes = int(final_format[4])
#seconds = int(final_format[5])
#
#print(year,month,day,hours,minutes,seconds)
#
#
#first_time = datetime.datetime(year,month,day,hours,minutes,seconds)
#later_time = datetime.datetime.now()
#dif = later_time - first_time
#datetime.timedelta(0, 8, 562000)
#print(dif)
#
##
##time = new_d_arr[0][2][2:]
##print(time[1])
#user_login = {'Type': 'Log_In', 'email': "email", 'password': "password"}
#Login_arr = pickle.dumps(user_login)
#print(Login_arr)

home_data_string = [(1, 'static\\image\\note_20 ultra.png', 'Note 20 ultra', 'Phone', 'ACTIVE', 235000.0, datetime.datetime(2022, 1, 4, 0, 0)), (2, 'static\\image\\iphone_13 pro.png', 'Apple 13 Pro', 'Phone', 'ACTIVE', 250000.0, datetime.datetime(2022, 1, 5, 0, 0)), (3, 'static\\image\\iphone_13 pro.png', 'Apple 13 pro max', 'Phone', 'ACTIVE', 280000.0, datetime.datetime(2022, 1, 6, 0, 0)), (4, 'static\\image\\note_20 ultra.png', 'Note 20', 'Phone', 'Available', 220000.0, datetime.datetime(2022, 1, 7, 0, 0)), (5, 'static\\image\\note_20 ultra.png', 'Note 20 Mini', 'Phone', 'Available', 150000.0, datetime.datetime(2022, 1, 8, 0, 0)), (6, '', 'apple', 'Phone', 'sf', 54156.0, datetime.datetime(2022, 1, 9, 0, 0)), (7, 'static\\image\\note_20 ultra.png', 'Note 20 Pro ', 'Phone', 'Available', 280000.0, datetime.datetime(2022, 1, 10, 0, 0)), (9, 'static\\image\\note_20 ultra.png', 'Samsung Note 20', 'Phone', 'Available', 320000.0, datetime.datetime(2022, 1, 3, 0, 0))]
#for details in home_data_string:
#    Item_ID= details[0]
#    Item_Image = details[1]
#    Item_Title = details[2]
#    Item_Category = details[3]
#    Item_Status = details[4]
#    Item_Base_Price = details[5]
#    Item_Expiry_Date = details[6]
#    g = "lol"
#
#
#
#    print(Item_Owner_Id,Item_Image, Item_Title, Item_Category,Item_Base_Price,Item_Expiry_Date,Item_Details,Item_Status)
#final_date = []
#for details in home_data_string:
#    temp_date = [details]
#    Item_Expiry_Date = str(temp_date[0][6])
#    #print(Item_Expiry_Date)
#    date = Item_Expiry_Date
#
#    time_format = date.replace(":", ",")
#    date_format = time_format.replace("-", ",")
#    final_raw_format = date_format.replace(" ", ",")
#    final_format = final_raw_format.rsplit(',')
#    year = int(final_format[0])
#    month = int(final_format[1])
#    day = int(final_format[2])
#
#    hours = int(final_format[3])
#    minutes = int(final_format[4])
#    seconds = int(final_format[5])
#
#    dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
#    "2022 - 01 - 04 00: 00:00"
#    temp_date.append(dates)
#    final_date.append(temp_date)
#
##print(final_date[0][1])
#
#    #print(year, month, day, hours, minutes, seconds)
#    c = "2022-01-04 00:00:00"
#    first_time = datetime.datetime(2022, 1, 2, 23, 11, 15)
#    later_time = datetime.datetime(2022, 1, 3, 0, 0, 0)
#    dif = later_time - first_time
#    datetime.timedelta(0, 8, 562000)
#    print(dif)
#
#    final_dif = str(dif)
#    #print("data = ", final_dif)
#    temp_date.append(final_dif)
#    final_date.append(temp_date)
#    #print(g)
##
##print(final_date)
#ff = ['2022-1-4 0:0:0', '2022-1-5 0:0:0', '2022-1-6 0:0:0', '2022-1-7 0:0:0', '2022-1-8 0:0:0', '2022-1-9 0:0:0', '2022-1-10 0:0:0']
##for i in range(0,len(ff)):
##    print(ff[i])
#
#
#
#item_data_string = [(1, 1, 'static\\image\\note_20 ultra.png', 'Note 20 ultra', 'Phone', 235000.0, datetime.datetime(2022, 1, 4, 0, 0), '12GB RAM', None, None, 'ACTIVE', None)]
#Item_Expiry_Date = item_data_string[0][6]
#print(Item_Expiry_Date)
#
#
#gg = {'Item_Result': [(1, 1, 'static\\image\\note_20 ultra.png', 'Note 20 ultra', 'Phone', 235000.0, datetime.datetime(2022, 1, 4, 0, 0), '12GB RAM', None, None, 'ACTIVE', None)], 'Max_Bid_Result': [(500000.0,)]}
#print(gg["Item_Result"])
#cc = gg["Max_Bid_Result"]
#print(cc[0][0])
#
#from datetime import datetime
#
#now = datetime(2022, 1, 2, 13, 32, 10)
#then = datetime(2022, 1, 2, 13, 32, 00)
#duration = now - then
#duration_in_s = duration.total_seconds()
#print(duration_in_s)

import random
import socket
import struct
import mysql.connector
import datetime

data_base = mysql.connector.connect(
    host='127.0.0.3',
    user='root',
    passwd='root',
    database='cmp_mini'
)

db_01 = data_base.cursor()


#def bid_end():
#    item_sql = """SELECT item_id, item_expiry_date FROM cmp_mini.items;"""
#    db_01.execute(item_sql)
#    item_result = db_01.fetchall()
#    #print(home_result)
#    bid_ended_items = []
#    while True:
#        for i in range(0, len(item_result)):
#            arr = str(item_result[i][1])
#            year = int(arr[:4])
#            month = int(arr[5:][:2])
#            day = int(arr[8:][:2])
#            hours = int(arr[11:][:2])
#            minutes = int(arr[14:][:2])
#            seconds = int(arr[17:][:2])
#            dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
#            now = datetime.datetime.now()
#            end_time = datetime.datetime(year, month, day, hours, minutes, seconds)
#            #end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
#            duration = end_time - now
#            duration_in_s = duration.total_seconds()
#            #print(duration_in_s)
#            if duration_in_s < 60:
#                item_id = item_result[i][0]
#                max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
#                db_01.execute(max_bid_sql)
#                max_bid_result = db_01.fetchall()
#                bid_ended_items.append(max_bid_result)
#
#        #print(bid_ended_items)
#        for update_item in bid_ended_items:
#            #print(update_item)
#            bid_item_id = update_item[0][0]
#            bid_buyer_id = update_item[0][1]
#            sold_price = update_item[0][2]
#            #print(bid_item_id,bid_buyer_id,sold_price)
#


#        print("Final_Bid_Updated")
#        break
#    print("end")
#
#
#bid_end()
#
#while True:
#    bb = (socket.inet_ntoa(struct.pack('>I', random.randint(0xf0000000, 0xffffffff))))
#    #print(bb)
#    #print(bb[:3])
#    y = int(bb[:3])
#    print(bb)
#    if y < 240:
#        print(bb)
#        break

#bid_notificatin_sql = "SELECT DISTINCT bid_buyer_id FROM bid_item WHERE bid_item_id = 1;"
#db_01.execute(bid_notificatin_sql)
#bid_notificatint_arr = db_01.fetchall()
#print(bid_notificatint_arr)
#
#for user in bid_notificatint_arr:
#    print(user[0])
#
#Phone_Number = "0774515356"
#
#
#user_id_find_sql = "SELECT DISTINCT bid_buyer_id FROM bid_item WHERE bid_item_id = %s;" % Item_ID
#db_01.execute(user_id_find_sql)
#user_id_arr = db_01.fetchall()
#print(user_id_arr)
#
#user_id = user_id_arr[1][0]
#print(user_id)
#
#user_data_arr = [(1, 'Pasindu', 'Sahan', '0774515356', 'pasindusahan001@gmail.com', '437/2 Palanwaththa, Pannipitiya')]
#print(user_data_arr[0][0])

#Item_ID = 2
#sub_user_sql = "SELECT DISTINCT bid_buyer_id FROM bid_item WHERE bid_item_id = %s;" % Item_ID
#db_01.execute(sub_user_sql)
#sub_user = db_01.fetchall()
#print(sub_user)
#
#user_id = sub_user[1][0]
#print(user_id)
#sub_user_arr = []
#for i in sub_user:
#    print(i[0])
#    sub_user_arr.append(i[0])
#
#broadcast_ip_arr =[]
#for i in sub_user_arr:
#    sub_user_broadcast_IP_sql = "SELECT broadcast_IP FROM multicast WHERE user_id = %s;" % i
#    db_01.execute(sub_user_broadcast_IP_sql)
#    broadcast_IP = db_01.fetchall()
#    #print(broadcast_IP[0][0])
#    if broadcast_IP[0][0] != None:
#        print("lol")
#        broadcast_ip_arr.append(broadcast_IP[0][0])

#print(sub_user_arr)
#print(broadcast_ip_arr)

#Broadcast_Data = {'Image': 'static\\image\\note_20 ultra.png', 'Title': 'Redda', 'Base_Price': '280000', 'Expiry_Date': '2022-01-12'}
#Broadcast_Sub_Data = {"Type": "New_Bid", 'Item_ID': '1', 'Title': 'Note 20 ultra', 'Base_Price': 235000.0, 'Max_bid': 500036.0}
#
#Type = Broadcast_Sub_Data["Type"]
#Title = Broadcast_Sub_Data["Title"]
#Base_Price = Broadcast_Sub_Data["Base_Price"]
#Max_bid = Broadcast_Sub_Data["Max_bid"]
#
#Type = Broadcast_Sub_Data["Type"]
#Title = Broadcast_Data["Title"]
#Base_Price = Broadcast_Data["Base_Price"]
#Expiry_Date = Broadcast_Data["Expiry_Date"]
#
#for i in range(0,5):
#    print(i)

#print(Broadcast_Sub_Data["Title"])

#item_sql = """SELECT item_id, item_expiry_date FROM cmp_mini.items;"""
#db_01.execute(item_sql)
#item_result = db_01.fetchall()
##print(home_result)
#bid_ended_items = []
#print(item_result)
#while True:
#    for i in range(0, len(item_result)):
#        arr = str(item_result[i][1])
#        year = int(arr[:4])
#        month = int(arr[5:][:2])
#        day = int(arr[8:][:2])
#        hours = int(arr[11:][:2])
#        minutes = int(arr[14:][:2])
#        seconds = int(arr[17:][:2])
#        #dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
#        now = datetime.datetime.now()
#        end_time = datetime.datetime(year, month, day, hours, minutes, seconds)
#        #end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
#        duration = end_time - now
#        duration_in_s = duration.total_seconds()
#        #print(duration_in_s)
#        if duration_in_s < 60:
#            item_id = item_result[i][0]
#            print(item_id)
#            max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
#            db_01.execute(max_bid_sql)
#            max_bid_result = db_01.fetchall()
#            bid_ended_items.append(max_bid_result)
#
#    #print(bid_ended_items)
#    for update_item in bid_ended_items:
#        #print(update_item)
#        bid_item_id = update_item[0][0]
#        bid_buyer_id = update_item[0][1]
#        sold_price = update_item[0][2]
#        #print(bid_item_id,bid_buyer_id,sold_price)
#
#        final_bid_sql = "UPDATE items SET item_buyer = %s, item_sold_price = %s WHERE item_id = %s;"
#        val = (bid_buyer_id, sold_price, bid_item_id)
#        db_01.execute(final_bid_sql, val)
#        data_base.commit()
#    print("Final_Bid_Updated")
#    break
#print("end")
#
#while True:
#    now = datetime.datetime.now()
#    #print(now)
#
#    arr = str(now)
#    year = int(arr[:4])
#    month = int(arr[5:][:2])
#    day = int(arr[8:][:2])
#    hours = int(arr[11:][:2])
#    minutes = int(arr[14:][:2])
#    seconds = int(arr[17:][:2])
#    dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
#    now = datetime.datetime.now()
#    end_time = datetime.datetime(year, month, day, hours, minutes, seconds)
#    # end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
#    duration = end_time - now
#    duration_in_s = duration.total_seconds()
#    # print(duration_in_s)
#
#    if hours == 23 and minutes == 58 and seconds == 30:
#        print("lol")
#        break
#
#import time
#
#result = time.gmtime(1545925769)
#print("result:", result)
#print("\nyear:", result.tm_year)
#print("tm_hour:", result.tm_hour)

def expire_time_calculate(date):
    while True:
        now = date
        # print(now)

        arr = now
        year = int(arr[:4])
        month = int(arr[5:][:2])
        day = int(arr[8:][:2])
        hours = int(arr[11:][:2])
        minutes = int(arr[14:][:2])
        seconds = int(arr[17:][:2])
        dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
        now = datetime.datetime.now()
        end_time = datetime.datetime(year, month, day, hours, minutes, seconds)
        # end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
        duration = end_time - now
        #print(duration)
        #print(day)
        duration_in_s = duration.total_seconds()
        #print(duration_in_s)
        #and hours == 23 and minutes == 58 and seconds == 30

        if 60 >= duration_in_s > 0:
            end_time = duration_in_s + 60
            print("lol")
            print(end_time)

            return end_time

        return duration_in_s


#print(expire_time_calculate("2022-01-10 07:40:00"))


#def bid_end_check(Expiry_Date):
#    while True:
#        arr = Expiry_Date
#        year = int(arr[:4])
#        month = int(arr[5:][:2])
#        day = int(arr[8:][:2])
#        hours = int(arr[11:][:2])
#        minutes = int(arr[14:][:2])
#        seconds = int(arr[17:][:2])
#        dates = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
#        now = datetime.datetime.now()
#        end_time = datetime.datetime(year, month, day, hours, minutes, seconds)
#        # end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
#        duration = end_time - now
#        duration_in_s = duration.total_seconds()
#        #print(duration_in_s)
#
#        return duration_in_s
#
#import schedule
#import time
#
#def job():
#    print("I'm working...")
#
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
#
#while True:
#    schedule.run_pending()
#    time.sleep(1)
#from datetime import datetime
#import pandas
#
#x = "2022-01-12 23:59:40"
#'%Y/%m/%d %H:%M:%S'
#time_str = x
#date_format_str = '%Y-%m-%d %H:%M:%S'
#
#given_time = datetime.strptime(time_str, date_format_str)
#print('Given timestamp: ', given_time)
#
#n = 1
#final_time = given_time + pandas.DateOffset(minutes=n)
#final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
#print('Final Time as string object: ', final_time_str)
#
#
#x = "2022-01-10 13:01:50"
#time_str = x
#date_format_str = '%Y-%m-%d %H:%M:%S'
#given_time = datetime.strptime(time_str, date_format_str)
#
#
#now = "2022-01-10 13:00:40"
#given = datetime.strptime(now, date_format_str)
#
#duration = given_time - given
#duration_in_s = duration.total_seconds()
#print(duration_in_s)
#from datetime import datetime
#import time
#
#time_str = "2022-01-10 13:15:00"
#date_format_str = '%Y-%m-%d %H:%M:%S'
#expiry_time = datetime.strptime(time_str, date_format_str)
#now = datetime.now()
#now_01 = str(datetime.now())
#print("NOW", now)
#print("NOW", now_01)
#now_02 = (now_01[:19])
## end_time = datetime.datetime(2022, 1, 2, 14, 30, 50)
#ex = datetime.strptime(now_02, date_format_str)
#
#duration = expiry_time - ex
#duration_in_s = duration.total_seconds()
#print("Final", duration_in_s)
#
#ex = datetime.strptime(now_02, date_format_str)
#n = 1
#final_time = ex + pandas.DateOffset(minutes=n)
#final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
#print("Final_time", final_time_str)
#
#
#item_sql = """SELECT item_id, item_expiry_date FROM cmp_mini.items;"""
#db_01.execute(item_sql)
#item_result = db_01.fetchall()
##print(home_result)
#bid_ended_items = []
#print(item_result)
#
#for i in range(0, len(item_result)):
#    arr = str(item_result[i][1])
#    date_format_str = '%Y-%m-%d %H:%M:%S'
#    expiry_time = datetime.strptime(arr, date_format_str)
#    now_01 = str(datetime.now())
#    now_02 = (now_01[:19])
#    ex = datetime.strptime(now_02, date_format_str)
#    duration = expiry_time - ex
#    duration_in_s = duration.total_seconds()
#    print("Final", duration_in_s)
#
#    if duration_in_s < 60:
#        item_id = item_result[i][0]
#        max_bid_sql = "SELECT bid_item_id, bid_buyer_id, max(bid_price) FROM bid_item WHERE bid_item_id = %s;" % item_id
#        db_01.execute(max_bid_sql)
#        max_bid_result = db_01.fetchall()
#        bid_ended_items.append(max_bid_result)
#
#print(bid_ended_items)
#

#all_user = [('224.0.0.0',), ('224.0.0.1',)]
#for i in range(0, len(all_user)):
#    print(all_user[i][0])

#dashboard_own_items_result = [(1, 'Note 20 ultra', 235000.0), (4, 'Note 20', 220000.0), (5, 'Note 20 Mini', 150000.0), (7, 'Note 20 Pro ', 280000.0), (9, 'Samsung Note 20', 320000.0), (10, 'Test_01', 320000.0), (42, 'Title', 690000.0), (43, 'Acc Check', 320000.0), (44, 'Final Test', 690000.0), (46, 'New_Item', 320000.0), (47, '012', 320000.0), (48, 'fd', 220000.0), (49, 'kkl', 320000.0), (50, 'ddd', 320000.0), (51, 'aaa', 690000.0), (52, 'aa', 220000.0), (53, 'aa', 280000.0), (54, 'vv', 280000.0), (55, 'lol', 320000.0), (56, 'dd', 690000.0), (58, 'qwe', 220000.0), (59, 'ww', 690000.0)]
#x = []
#c = []
#
#
#for i in dashboard_own_items_result:
#    #temp_id = dashboard_own_items_result[i][0]
#    #temp_title = dashboard_own_items_result[i][1]
#    #temp_base_price = dashboard_own_items_result[i][2]
#    #temp_max = "202"
#    #re_create = f""" ({temp_id},{temp_title},{temp_base_price},{temp_max})"""
#    #tup = (temp_id,temp_title,temp_base_price,temp_max)
#    #c.append(tup)
#    print(i[0])

import pandas
from datetime import datetime
import schedule
import time

data_string = {'Type': 'New_Item', 'Sub_Type': 'Special', 'Owner_ID': '1', 'Image': 'static\\image\\note_20 ultra.png', 'Title': 'House_06', 'Category': 'House', 'Base_Price': '690000', 'Expiry_Date': '1', 'Main_Details': '3 Rooms And 1 Kitchen', 'Details': 'Well maintained '}

Expiry_Date_raw = data_string["Expiry_Date"]
Expiry_Date = int(Expiry_Date_raw)


current_time = str(datetime.now())
current_time_expand = current_time[:19]
date_format_str = '%Y-%m-%d %H:%M:%S'
time_convert = datetime.strptime(current_time_expand, date_format_str)
print("time_convert", time_convert)
extended_time = 20
final_time = time_convert + pandas.DateOffset(seconds=extended_time)
final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
print("final_time_str", final_time_str)
gg = str(final_time_str[11:])

print(gg)

def test():
    print("Gammac Thamai")

schedule.every().day.at(gg).do(test)

def clock():
    while True:
        schedule.run_pending()
        time.sleep(0.5)

clock()

