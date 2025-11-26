import requests
import xml.etree.ElementTree as ET
import streamlit as st

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

respuesta = requests.get(url)

datos_xml = ET.fromstring(respuesta.content)

tasas = {}
fecha_actualizacion = "Desconocida"

for linea in datos_xml.iter():

    if 'time' in linea.attrib:
        fecha_actualizacion = linea.attrib['time']

    if 'currency' in linea.attrib:
        moneda = linea.attrib['currency']
        valor = float(linea.attrib['rate'])
        tasas[moneda] = valor

tasas['EUR'] = 1.0

st.title("Conversor de Divisas")

st.write("Fecha de los datos: " + fecha_actualizacion)

cantidad = st.number_input("Cantidad a convertir", value=100.0)
lista_monedas = sorted(tasas.keys())

moneda_origen = st.selectbox("Moneda de Origen", lista_monedas)
moneda_destino = st.selectbox("Moneda de Destino", lista_monedas)

if st.button("Calcular"):

    valor_origen = tasas[moneda_origen]
    valor_destino = tasas[moneda_destino]

    resultado = (cantidad / valor_origen) * valor_destino

    st.write("El resultado es:", resultado)