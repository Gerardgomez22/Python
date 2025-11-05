import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://books.toscrape.com/'

print("Enviando petición a:", URL)
pagina = requests.get(URL)
soup = BeautifulSoup(pagina.content, 'html.parser')

libros = soup.find_all('article', class_='product_pod')

datos_libros = []

rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

print(f"Se encontraron {len(libros)} libros. Extrayendo datos...")

for libro in libros:
    
    titulo = libro.h3.a['title']

    precio_texto = libro.find('p', class_='price_color').text
    precio = float(precio_texto.replace('£', ''))

    rating_clase = libro.find('p', class_='star-rating')['class'][1]
    rating_num = rating_map.get(rating_clase, 0) 

    disponibilidad = libro.find('p', class_='instock availability').text.strip()

    url_imagen = URL + libro.find('img', class_='thumbnail')['src']

    datos_libros.append({
        'Titulo': titulo,
        'Precio': precio,
        'Rating': rating_num,
        'Disponibilidad': disponibilidad,
        'URL_Imagen': url_imagen
    })

print("Creando DataFrame con los datos...")
df = pd.DataFrame(datos_libros)

df.to_csv('libros.csv', index=False, encoding='utf-8')

print("¡Proceso completado! Los datos se han guardado en 'libros.csv'")
