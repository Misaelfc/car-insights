import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.write(car_data.columns)
# Encabezado
st.header("Análisis de Vehículos Usados")
# Casilla de verificación para histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para el kilometraje de los vehículos')
    fig = px.histogram(
        car_data, x="odometer", nbins=50,
        title="Distribución del kilometraje"
    )
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs kilometraje')
    fig = px.scatter(
        car_data, x="odometer", y="price", color="condition",
        title="Precio vs Kilometraje según condición del vehículo"
    )
    st.plotly_chart(fig, use_container_width=True)

# Casilla para comparar precios de vehículos entre manufactureras
build_prices = st.checkbox('Comparar precios de vehículos')
if build_prices:
    st.write('Comparación de precios de vehículos entre diferentes manufactureras')
    fig = px.box(
        car_data, x="model", y="price", color="condition",
        title="Comparación de precios por fabricante"
    )
    st.plotly_chart(fig, use_container_width=True)
