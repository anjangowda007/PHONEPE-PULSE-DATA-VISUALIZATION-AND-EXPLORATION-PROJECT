import streamlit as st
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2,3,4,5,6,]
plt.hist(x, y)

# Use st.pyplot() to display the Matplotlib plot in Streamlit
st.pyplot()
