import streamlit as st
import numpy as np
from scipy.optimize import minimize

def optimize_fun(x):
    return x[0]**2 + x[1]**2

st.title("Optimization Web App")

st.write("This app demonstrates an optimization example using the scipy library.")

st.write("Please enter the initial values for the optimization process.")

x0 = st.number_input("x0:")
y0 = st.number_input("y0:")

res = minimize(optimize_fun, [x0, y0])

st.write("Optimization results:")
st.write("x = ", res.x[0])
st.write("y = ", res.x[1])
