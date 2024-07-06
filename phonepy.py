import mysql.connector
import pandas as pd
import json
import os
path1 = "C:/Users/Senthil/Downloads/phonepe/pulse/data/aggregated/transaction/country/india/state/"


agg_tran_list = os.listdir(path1)

columns1 ={"States":[], "Years":[], "Quarter":[], "Transaction_type":[], "Transaction_count":[],"Transaction_amount":[] }

for state in agg_tran_list:
    cur_states =path1+state+"/"
    agg_year_list = os.listdir(cur_states)
    
    for year in agg_year_list:
        cur_years = cur_states+year+"/"
        agg_file_list = os.listdir(cur_years)

        for file in agg_file_list:
            cur_files = cur_years+file
            data = open(cur_files,"r")
            A = json.load(data)

            for i in A["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))

aggre_transaction = pd.DataFrame(columns1)


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

create_query1 = '''CREATE TABLE if not exists type_of_pay (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
cursor.execute(create_query1)
connection.commit()

for index,row in aggre_transaction.iterrows():
    insert_query1 = '''INSERT INTO type_of_pay (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
data_to_insert = aggre_transaction.to_records(index=False).tolist()

# Use executemany to insert multiple rows
cursor.executemany(insert_query1, data_to_insert)
connection.commit()