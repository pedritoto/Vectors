import streamlit as st
import matplotlib.pyplot as plt
st.title("App para suma de vectores")
st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")
Ax = st.slider('Magnitud del vector A', 0, 10, 2)
Ay = st.slider('Magnitud del vector B', 0, 10, 2)
Bx = st.slider('Dirección del vector A', 0, 360, 10,0.05)
By = st.slider('Dirección del vector B', 0, 360, 45,0.05)

