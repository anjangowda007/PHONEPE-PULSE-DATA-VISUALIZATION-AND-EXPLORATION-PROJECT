import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.express as px
import mysql.connector
import streamlit as st

host = "localhost"
user = "root"
password = "PrasHantHCHinnapappal19802003"
connection = mysql.connector.connect(
           host=host,
           user=user,
           password=password
            )
cursor = connection.cursor()
cursor.execute('USE phone_pe')
# Assuming you have a cursor and a connection set up (not shown in your provided code)

# SQL query
sql_query2 = """
    SELECT States, Transaction_type
    FROM type_of_pay
    WHERE Years = 2018 AND Quarter = 3 AND Transaction_type = 'Recharge & bill payments' AND States != 'Lakshadweep'
    ORDER BY States ASC"""
cursor.execute(sql_query2)
results = cursor.fetchall()

# Create a DataFrame
# df = pd.DataFrame(results, columns=['States', 'Transaction_type'])
import pandas as pd

data = {
  'States' :[
    "Andaman & Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra & Nagar Haveli & Daman & Diu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu & Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
],
 'Latitude': [
        15.9129, 28.2180, 26.2006, 25.0961, 21.2787,
        15.2993, 22.2587, 29.0588, 32.2396, 23.6102,
        15.3173, 10.8505, 22.9734, 19.7515, 24.6637,
        25.4670, 23.1645, 26.1584, 20.9517, 31.1471,
        30.9000, 27.0238, 27.5330, 11.1271, 18.1124,
        23.9408, 26.8467, 28.6304,25.000,58.0000,85.0000,98.000,98.7000,58.0000,87.0000,96.0000
    ],
    'Longitude': [
        79.7400, 94.7278, 92.9376, 85.3131, 81.8661,
        74.1240, 71.1924, 76.0856, 77.8375, 85.2799,
        75.7131, 76.2711, 78.6569, 75.7139, 93.9063,
        91.3662, 92.9376, 94.5624, 85.0985, 76.1937,
        75.5000, 74.2179, 88.6065, 78.6569, 79.0193,
        91.9882, 80.9462, 77.1025, 87.000,85.000,85.0000,98.000,98.7000,58.000,87.0000,96.0000
    ],
    'value' : [ 100,100,100,100,100,100,100, 200, 122,123, 150, 120, 180, 250, 300, 90, 160, 220, 130, 170, 240, 190, 110, 140, 200, 250, 160, 180, 120, 190, 150, 210, 170, 230, 260, 140]
}

df = pd.DataFrame(data)

# Create a new column 'Value' with arbitrary values (replace these with your actual values)

# Display the updated DataFrame
# print(df)


# Streamlit app
st.title('Choropleth Map Example')

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='States',
    color='value',
    color_continuous_scale='Reds',
    title='Transaction Count Choropleth Map'
)

fig.update_geos(fitbounds="locations", visible=False)

# Display the choropleth map in Streamlit
st.plotly_chart(fig)
