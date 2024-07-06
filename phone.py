import mysql.connector
import pandas as pd
import json
import os
path2 = "C:/Users/Senthil/Downloads/phonepe/pulse/data/aggregated/user/country/india/state/"

agg_user_list=os.listdir(path2)
#Agg_state_list--> to get the list of states in India

#This is to extract the data's to create a dataframe
columns2 = {"States":[], "Years":[], "Quarter":[], "Brands":[],"Transaction_count":[], "Percentage":[]}

for state in agg_user_list:
    cur_states = path2+state+"/"
    agg_year_list = os.listdir(cur_states)
    for year in agg_year_list:
        cur_years = cur_states+year+"/"
        agg_file_list = os.listdir(cur_years)
        for file in agg_file_list:
            cur_files = cur_years+file
            with open(cur_files, "r") as data:
              B = json.load(data)
              try:
                  
                for y in B['data']['usersByDevice']:
                   brand = y["brand"]
                   count = y["count"]
                   percentage = y["percentage"]
                   columns2["Brands"].append(brand)
                   columns2["Transaction_count"].append(count)
                   columns2["Percentage"].append(percentage)
                   columns2["States"].append(state)
                   columns2["Years"].append(year)
                   columns2["Quarter"].append(int(file.strip(".json")))
                   
              except:
                  pass
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(columns2)
# print(Agg_Trans)


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

# Create the 'type_of_brand' table
create_query1 = '''
CREATE TABLE IF NOT EXISTS type_of_brand (
    States VARCHAR(50),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(50),
    Transaction_count BIGINT,
    Percentage float
)
'''
cursor.execute(create_query1)
connection.commit()

# Assuming Agg_Trans is a DataFrame containing your data
insert_info = '''
INSERT INTO type_of_brand (States, Years, Quarter, Transaction_type, Transaction_count,Percentage)
VALUES (%s, %s, %s, %s, %s, %s)
'''

# Convert DataFrame to list of tuples for executemany
data_to_insert = Agg_Trans.to_records(index=False).tolist()

# Use executemany to insert multiple rows
cursor.executemany(insert_info, data_to_insert)
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
