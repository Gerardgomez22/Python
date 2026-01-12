import requests

BASE_URL = "http://127.0.0.1:5000/api/games"

def probar_todo():
    print("--- 1. PROBANDO CREAR (POST) ---")
    nuevo_juego = {"title": "FIFA 24", "genre": "Deportes", "price": 70.0}
    resp = requests.post(BASE_URL, json=nuevo_juego)
    if resp.status_code == 201:
        id_juego = resp.json()['id']
        print(f" Juego creado con ID: {id_juego}")
    else:
        print(" Fallo al crear")
        return

    print("\n--- 2. PROBANDO LEER (GET) ---")
    resp = requests.get(BASE_URL)
    print(f" Lista actual: {resp.json()}")

    print(f"\n--- 3. PROBANDO EDITAR (PUT) ID {id_juego} ---")
    cambios = {"price": 35.50}
    requests.put(f"{BASE_URL}/{id_juego}", json=cambios)
    print(" Precio actualizado a 35.50")

    print(f"\n--- 4. PROBANDO BORRAR (DELETE) ID {id_juego} ---")
    requests.delete(f"{BASE_URL}/{id_juego}")
    print(" Juego eliminado")

    print("\n--- 5. COMPROBACIÓN FINAL ---")
    resp = requests.get(BASE_URL)
    print(f"Lista final (debería estar vacía o sin el ID {id_juego}): {resp.json()}")

if __name__ == "__main__":
    try:
        probar_todo()
    except Exception as e:
        print(" Asegúrate de que el servidor (main.py) sigue ejecutándose en otra terminal.")
        print(f"Error: {e}")