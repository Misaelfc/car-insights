import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
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

# Casilla para comparar precios de vehículos entre modelos
build_prices = st.checkbox('Comparar precios entre dos modelos de vehículos')
if build_prices:
    st.write('Comparación de precios entre dos modelos seleccionados')
    # Lista única y ordenada de modelos para seleccionar
    modelos = sorted(car_data['model'].dropna().unique())

    modelo1 = st.selectbox(
        'Selecciona el primer modelo', modelos, index=0
    )
    modelo2 = st.selectbox(
        'Selecciona el segundo modelo',
        modelos, index=1 if len(modelos) > 1 else 0
    )

    # Filtrar datos por modelos seleccionados
    df_filtrado = car_data[car_data['model'].isin([modelo1, modelo2])]
    fig = px.box(
        df_filtrado, x="model", y="price", color="condition",
        title=f"Comparación de precios: {modelo1} vs {modelo2}",
        labels={"model": "Modelo", "price": "Precio"}
    )
    st.plotly_chart(fig, use_container_width=True)
