import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
import mysql.connector


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



A = st.selectbox("select", ['Select',"Aggregated","Map","Top"])
Y = st.selectbox("Select",["Select","Transaction", "User"])



latitude_longitude_data = {
    'Latitude': [
        15.9129, 28.2180, 26.2006, 25.0961, 21.2787,
        15.2993, 22.2587, 29.0588, 32.2396, 23.6102,
        15.3173, 10.8505, 22.9734, 19.7515, 24.6637,
        25.4670, 23.1645, 26.1584, 20.9517, 31.1471,
        30.9000, 27.0238, 27.5330, 11.1271, 18.1124,
        23.9408, 26.8467, 28.6304, 25.000, 58.0000, 85.0000, 98.000, 98.7000, 58.0000, 87.0000, 96.0000
    ],
    'Longitude': [
        79.7400, 94.7278, 92.9376, 85.3131, 81.8661,
        74.1240, 71.1924, 76.0856, 77.8375, 85.2799,
        75.7131, 76.2711, 78.6569, 75.7139, 93.9063,
        91.3662, 92.9376, 94.5624, 85.0985, 76.1937,
        75.5000, 74.2179, 88.6065, 78.6569, 79.0193,
        91.9882, 80.9462, 77.1025, 87.000, 85.000, 85.0000, 98.000, 98.7000, 58.000, 87.0000, 96.0000
    ]
}

df_lat_lon = pd.DataFrame(latitude_longitude_data)

states = [
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
]
data = pd.DataFrame(states, columns=['states'])
# result_df = pd.concat([data, df_lat_lon], axis=1)


def geo4():
  sql_query2 = """
    SELECT SUM(RegisteredUser),  SUM(AppOpens)
    FROM register_user
    WHERE Years = %s AND Quarter = %s
    GROUP BY States
    ORDER BY States ASC"""
  cursor.execute(sql_query2,(B, C))
  results = cursor.fetchall()
  df1 = pd.DataFrame(results, columns = ['RegisteredUser',"AppOpens"])
  df4 = pd.concat([df_lat_lon,data ,df1], axis=1)
  return df4

def geoo4(Q):
  fig = px.choropleth(
    Q,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='states',
    # color='AppOpens',
    hover_data=['RegisteredUser',"AppOpens"],
    # color_continuous_scale='Reds',
    
)
  fig.update_geos(fitbounds="locations", visible=False)
  st.plotly_chart(fig)
  return 'success'

def geoo5(Q):
  fig = px.choropleth(
    Q,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='states',
    color='AppOpens',
    animation_frame='RegisteredUser',  
)
  fig.update_geos(fitbounds="locations", visible=False)
  st.plotly_chart(fig)
  return 'success'



if A == 'Map' and Y == 'User':
    if Y:
        B = st.selectbox("select Year", ['Select',"2018","2019","2020",'2021','2022','2023'])
        Years = B
        if B!='Select':
            C = st.selectbox("select Quarter", ['Select',"1","2","3",'4'])
            if C!='Select':
              S = geo4()
              if S is not None:
                geoo4(S)
                geoo5(S)
                
                






                
                
                
                
                
                
                

                
                
                
            
            
            
            
            

    
  
  


