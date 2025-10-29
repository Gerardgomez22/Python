# scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Definir la URL del sitio a scrapear
URL = 'http://books.toscrape.com/'

# 2. Realizar la petición HTTP a la página
print("Enviando petición a:", URL)
pagina = requests.get(URL)
soup = BeautifulSoup(pagina.content, 'html.parser')

# 3. Extraer la información de los libros
# Buscamos todos los contenedores de libros, que son <article> con la clase 'product_pod'
libros = soup.find_all('article', class_='product_pod')

# Lista para almacenar los datos extraídos
datos_libros = []

# Mapeo de la clase de rating a un número
rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

print(f"Se encontraron {len(libros)} libros. Extrayendo datos...")

# 4. Iterar sobre cada libro para obtener los detalles
for libro in libros:
    # Título del libro
    titulo = libro.h3.a['title']

    # Precio del libro (se extrae el texto y se limpia)
    precio_texto = libro.find('p', class_='price_color').text
    precio = float(precio_texto.replace('£', ''))

    # Rating (extraemos la clase que indica las estrellas, ej: "star-rating Three")
    rating_clase = libro.find('p', class_='star-rating')['class'][1]
    rating_num = rating_map.get(rating_clase, 0) # Convertimos el texto a número

    # Disponibilidad
    disponibilidad = libro.find('p', class_='instock availability').text.strip()

    # Enlace de la portada
    url_imagen = URL + libro.find('img', class_='thumbnail')['src']

    # Añadimos los datos a nuestra lista
    datos_libros.append({
        'Titulo': titulo,
        'Precio': precio,
        'Rating': rating_num,
        'Disponibilidad': disponibilidad,
        'URL_Imagen': url_imagen
    })

# 5. Guardar los datos en un archivo CSV usando Pandas
print("Creando DataFrame con los datos...")
df = pd.DataFrame(datos_libros)

# Guardar el DataFrame en un archivo CSV
df.to_csv('libros.csv', index=False, encoding='utf-8')

print("¡Proceso completado! Los datos se han guardado en 'libros.csv'")