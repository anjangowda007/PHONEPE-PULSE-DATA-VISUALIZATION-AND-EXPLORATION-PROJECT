import mysql.connector
import pandas as pd
import json
import plotly.express as px
import os
import streamlit as st


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
# cursor.execute('USE phone_pe')

# Create the 'phone_pe' database if it doesn't exist

cursor.execute('USE phone_pe')

query1 = """select distinct(States) from type_of_pay"""
cursor.execute(query1)
P = cursor.fetchall()
V = pd.DataFrame(P, columns =["States"])


def sun4(Q,W,E):
    query = """select Districts, RegisteredUser, AppOpens from register_user
     where States = %s and  Years = %s and Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=['District', 'RegisteredUser','AppOpens'])
    fig = px.sunburst(Z, path=['District', 'RegisteredUser','AppOpens'], hover_data={'District': True, 'RegisteredUser': True,'AppOpens':True} )
    fig.update_layout(width = 800,height = 700)
    fi = px.bar(Z, x ='District' , y = 'RegisteredUser')
    return fig, fi




Q = st.selectbox("Select",['Select States']+list(V['States']))
W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
    B ,n= sun4(Q, W, E)
    st.plotly_chart(B)
    st.plotly_chart(n)
    
    
    
                    







        



