import mysql.connector
import pandas as pd
import json
import os
path5 = "C:/Users/Senthil/Downloads/phonepe/pulse/data/top/transaction/country/india/state/"

top_tran_list=os.listdir(path5)

columns5 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state in top_tran_list:
    cur_states = path5+state+"/"
    top_year_list = os.listdir(cur_states)
    
    for year in top_year_list:
        cur_years = cur_states+year+"/"
        top_file_list = os.listdir(cur_years)
        
        for file in top_file_list:
            cur_files = cur_years+file
            data = open(cur_files,"r")
            E = json.load(data)

            for i in E["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                columns5["Pincodes"].append(entityName)
                columns5["Transaction_count"].append(count)
                columns5["Transaction_amount"].append(amount)
                columns5["States"].append(state)
                columns5["Years"].append(year)
                columns5["Quarter"].append(int(file.strip(".json")))

top_transaction = pd.DataFrame(columns5)

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
create_query5 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query5)
connection.commit()

# for index,row in top_transaction.iterrows():
insert_query5 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
data_to_insert = top_transaction.to_records(index=False).tolist()

# Use executemany to insert multiple rows
cursor.executemany(insert_query5, data_to_insert)
connection.commit()