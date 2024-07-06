import mysql.connector
import pandas as pd
import json
import os
path3 = "C:/Users/Senthil/Downloads/phonepe/pulse/data/map/transaction/hover/country/india/state/"

map_tran_list=os.listdir(path3)

columns3 = {"States":[], "Years":[], "Quarter":[],"District":[], "Transaction_count":[],"Transaction_amount":[]}

for state in map_tran_list:
    cur_states = path3+state+"/"
    map_year_list = os.listdir(cur_states)
    
    for year in map_year_list:
        cur_years = cur_states+year+"/"
        map_file_list = os.listdir(cur_years)
        
        for file in map_file_list:
            cur_files = cur_years+file
            data = open(cur_files,"r")
            C = json.load(data)

            for i in C['data']["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns3["District"].append(name)
                columns3["Transaction_count"].append(count)
                columns3["Transaction_amount"].append(amount)
                columns3["States"].append(state)
                columns3["Years"].append(year)
                columns3["Quarter"].append(int(file.strip(".json")))

map_transaction = pd.DataFrame(columns3)

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
create_query3 = '''CREATE TABLE if not exists transaction_count (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                District varchar(50),
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
cursor.execute(create_query3)
connection.commit()

# for index,row in map_transaction.iterrows():
insert_query3 = '''
                INSERT INTO Transaction_count (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

            '''
data_to_insert = map_transaction.to_records(index=False).tolist()

# Use executemany to insert multiple rows
cursor.executemany(insert_query3, data_to_insert)
connection.commit()

 