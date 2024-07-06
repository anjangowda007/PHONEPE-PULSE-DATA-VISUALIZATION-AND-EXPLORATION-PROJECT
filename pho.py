import mysql.connector
import pandas as pd
import json
import os
path4 = "C:/Users/Senthil/Downloads/phonepe/pulse/data/map/user/hover/country/india/state/"

map_user_list=os.listdir(path4)


columns4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for state in map_user_list:
    cur_states = path4+state+"/"
    map_year_list = os.listdir(cur_states)
    
    for year in map_year_list:
        cur_years = cur_states+year+"/"
        map_file_list = os.listdir(cur_years)
        
        for file in map_file_list:
            cur_files = cur_years+file
            data = open(cur_files,"r")
            D = json.load(data)

            for i in D["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                columns4["Districts"].append(district)
                columns4["RegisteredUser"].append(registereduser)
                columns4["AppOpens"].append(appopens)
                columns4["States"].append(state)
                columns4["Years"].append(year)
                columns4["Quarter"].append(int(file.strip(".json")))

map_user = pd.DataFrame(columns4)

host = "localhost"
user = "root"
password = "PrasHantHCHinnapappal19802003"

# Connect to MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
cursor = connection.cursor()

# Create the 'phone_pe' database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS phone_pe")
cursor.execute('USE phone_pe')
create_query4 = '''CREATE TABLE if not exists Register_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(50),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint)'''
cursor.execute(create_query4)
connection.commit()

# for index,row in map_user.iterrows():
insert_query4 = '''INSERT INTO Register_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                        values(%s,%s,%s,%s,%s,%s)'''
data_to_insert = map_user.to_records(index=False).tolist()

# Use executemany to insert multiple rows
cursor.executemany(insert_query4, data_to_insert)
connection.commit()