
import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

st.header('Bienvenido a mi proyecto del sprint 7')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la aplicación Streamlit para histograma
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    print('boton hist pulsado')
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
    print("grafico hist creado")

# crear una casilla para scatter
scat = st.checkbox('Construir un diagrama de dispersión')

if scat:
    print('boton scat pulsado')
    # Escribir un mensaje en la aplicación
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig2 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig2)
    print("grafico scat creado")


