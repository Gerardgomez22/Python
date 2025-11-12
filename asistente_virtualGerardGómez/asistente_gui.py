import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import os
from dotenv import load_dotenv

def leer_contexto(fichero='servicios.txt'):
    """Lee el fichero de texto con la información de la barbería."""
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo de contexto: {fichero}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
        return None

def generar_respuesta(pregunta):
    """Envía la pregunta y el contexto a la API de Gemini y devuelve la respuesta."""

    prompt_completo = f"""
    Eres un asistente virtual de la "Barberia GGA".
    Usa la siguiente información para responder las preguntas del cliente de forma amable y concisa.
    Si la pregunta no tiene que ver con la peluquería, dí amablemente que no puedes ayudar con eso.

    --- INFORMACIÓN DE CONTEXTO ---
    {CONTEXTO_PELUQUERIA}
    ---------------------------------
    
    Pregunta del cliente: "{pregunta}"
    
    Respuesta del asistente:
    """
    
    try:
        respuesta = model.generate_content(prompt_completo)
        return respuesta.text
    except Exception as e:
        print(f"Error en la API: {e}")
        return "Lo siento, he tenido un problema conectando con mis circuitos. Inténtalo de nuevo."

def enviar_pregunta():
    """Se ejecuta SOLAMENTE al pulsar el botón 'Enviar'."""
    pregunta = entrada_usuario.get() 
    
    if not pregunta.strip():
        return 

    actualizar_chat(f"Tú: {pregunta}\n")
    
    entrada_usuario.config(state='disabled')
    boton_enviar.config(state='disabled')
    
    respuesta_ia = generar_respuesta(pregunta)
    
    actualizar_chat(f"Asistente: {respuesta_ia}\n\n")
    
    entrada_usuario.delete(0, tk.END)
    
    entrada_usuario.config(state='normal')
    boton_enviar.config(state='normal')

def actualizar_chat(texto):
    """Añade texto a la ventana de chat (ScrolledText)."""
    chat_area.config(state='normal') 
    chat_area.insert(tk.END, texto) 
    chat_area.see(tk.END) 
    chat_area.config(state='disabled') 

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    messagebox.showerror("Error Crítico", "No se encontró la 'API_KEY' en el archivo .env")
    exit() 

CONTEXTO_PELUQUERIA = leer_contexto()
if CONTEXTO_PELUQUERIA is None:
    exit() 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('models/gemini-flash-latest')
except Exception as e:
    messagebox.showerror("Error de API", f"Error configurando Gemini. ¿API Key correcta?\n{e}")
    exit()

ventana = tk.Tk()
ventana.title("Asistente de Barberia GGA")
ventana.geometry("500x600")

frame_principal = tk.Frame(ventana, padx=10, pady=10)
frame_principal.pack(expand=True, fill='both')

chat_area = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD, state='disabled', font=("Arial", 11))
chat_area.pack(expand=True, fill='both', padx=5, pady=5)

frame_entrada = tk.Frame(frame_principal)
frame_entrada.pack(fill='x', padx=5, pady=5)

entrada_usuario = tk.Entry(frame_entrada, font=("Arial", 12))
entrada_usuario.pack(side=tk.LEFT, expand=True, fill='x', ipady=5)

boton_enviar = tk.Button(frame_entrada, text="Enviar", command=enviar_pregunta, font=("Arial", 10, "bold"))
boton_enviar.pack(side=tk.RIGHT, padx=5)

actualizar_chat("Bienvenido al Asistente de Barberia GGA.\nEscribe tu pregunta abajo y presiona 'Enviar'.\n\n")

ventana.mainloop()