import streamlit as st
import pandas as pd

try:
    df = pd.read_csv('libros.csv')
except FileNotFoundError:
    st.error("Error: No se encontró el archivo 'libros.csv'. Asegúrate de ejecutar primero el script 'scraper.py'.")
    st.stop() 

st.set_page_config(page_title="Dashboard de Libros", layout="wide")
st.title(' Dashboard Interactivo de Libros')
st.write("Explorador de datos de la web 'Books to Scrape'.")

st.sidebar.header('Filtros')

precio_seleccionado = st.sidebar.slider(
    'Filtrar por Precio:',
    min_value=float(df['Precio'].min()), 
    max_value=float(df['Precio'].max()),
    value=(float(df['Precio'].min()), float(df['Precio'].max())) 
)

rating_seleccionado = st.sidebar.slider(
    'Filtrar por Rating (estrellas):',
    min_value=1,
    max_value=5,
    value=(1, 5) 
)

df_filtrado = df[
    (df['Precio'] >= precio_seleccionado[0]) & (df['Precio'] <= precio_seleccionado[1]) &
    (df['Rating'] >= rating_seleccionado[0]) & (df['Rating'] <= rating_seleccionado[1])
]

st.header('Resultados del Filtro')
st.dataframe(df_filtrado)
st.write(f"Se encontraron {df_filtrado.shape[0]} libros con los filtros aplicados.")

st.header('Visualizaciones Gráficas')

st.subheader('Distribución de Libros por Rating')

rating_counts = df_filtrado['Rating'].value_counts().sort_index()

st.bar_chart(rating_counts)
