import csv

alumnos = {}

with open('notas_alumnos_UF1.csv', 'r') as file_uf1:
    lector_uf1 = csv.DictReader(file_uf1, delimiter=';')
    for fila in lector_uf1:
        id_alumno = fila['Id']
        alumnos[id_alumno] = fila

with open('notas_alumnos_UF2.csv', 'r') as file_uf2:
    lector_uf2 = csv.DictReader(file_uf2, delimiter=';')
    for fila in lector_uf2:
        id_alumno = fila['Id']
        if id_alumno in alumnos:
            alumnos[id_alumno]['UF2'] = fila['UF2']

nombres_columnas = ['Id', 'Apellidos', 'Nombre', 'UF1', 'UF2']

with open('notas_alumnos.csv', 'w', newline='') as archivo_salida:
    escritor = csv.DictWriter(archivo_salida, fieldnames=nombres_columnas, delimiter=';')
    
    escritor.writeheader()
    for id_alumno in alumnos:
        escritor.writerow(alumnos[id_alumno])

print("El archivo 'notas_alumnos.csv' se ha creado con éxito.")