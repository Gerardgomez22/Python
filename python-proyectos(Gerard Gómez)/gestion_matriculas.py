import os

NOMBRE_ARCHIVO = 'alumnos.txt'

def mostrar_menu():
    print("\n--- Menú de Matrículas ---")
    print("1) Matricular alumno")
    print("2) Listar alumnos")
    print("3) Eliminar archivo de alumnos")
    print("4) Salir")
    print("--------------------------")

def matricular_alumno():
    nombre = input("Introduce el nombre del alumno: ")
    
    # Abrimos en modo 'a' para añadir al final del fichero
    with open(NOMBRE_ARCHIVO, 'a') as archivo:
        archivo.write(nombre + "\n")
        
    print(f"'{nombre}' ha sido matriculado.")

def listar_alumnos():
    print("\n--- Lista de Alumnos ---")
    
    # Primero, comprobar si el archivo existe
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("Todavía no hay alumnos matriculados.")
        return

    # Si existe, lo abrimos para leer
    with open(NOMBRE_ARCHIVO, 'r') as archivo:
        alumnos = archivo.readlines()
        
        if not alumnos:
            print("El archivo está vacío.")
        else:
            for nombre_linea in alumnos:
                # Quitar el salto de línea final para que se vea bien
                print(f"- {nombre_linea.strip()}")
                
    print("------------------------")

def eliminar_archivo_alumnos():
    if os.path.exists(NOMBRE_ARCHIVO):
        os.remove(NOMBRE_ARCHIVO)
        print("Archivo de alumnos eliminado.")
    else:
        print("El archivo no existe, no se puede borrar.")

# --- Programa Principal ---
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        matricular_alumno()
    elif opcion == '2':
        listar_alumnos()
    elif opcion == '3':
        eliminar_archivo_alumnos()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")