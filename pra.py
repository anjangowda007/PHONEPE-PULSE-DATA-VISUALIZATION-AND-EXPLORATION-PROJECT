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

# selected_option = st.selectbox("Select an years", ["Select","2018", "2019","2020","2021","2022","2023"])
# selected_option1 = st.selectbox("Select Quarter", ["Select","1", "2","3","4"])
# # selected_option2 = st.selectbox("Select States",['Select State'] + state_options)
# Years = selected_option
# Quarter = selected_option1
# States = selected_option2



sql_query = """
    SELECT States, Transaction_type
    FROM type_of_pay
    WHERE Years = 2018 AND Quarter = 3 AND Transaction_type = 'Recharge & bill payments'
    ORDER BY Transaction_count DESC;
"""

# Execute SQL query
cursor.execute(sql_query)
results = cursor.fetchall()

# Create a Pandas DataFrame
Final = pd.DataFrame(results, columns=['States', 'Transaction_type'])
# print(Final)
# Close database connection
cursor.close()
connection.close()

# Create a choropleth map using Plotly Express
fig = px.choropleth(
    Final,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='States',
    color='Transaction_type',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig)