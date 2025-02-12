import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
import io
import requests

def obtener_datos_pokemon():
    nombre = entrada.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre_pokemon = datos["name"].capitalize()
        id_pokemon = datos["id"]
        altura = datos["height"] / 10
        peso = datos["weight"] / 10
        tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
        imagen_url = datos["sprites"]["front_default"]

        resultado.config(text=f"Nombre: {nombre_pokemon}\n"
                              f"ID: {id_pokemon}\n"
                              f"Altura: {altura} m\n"
                              f"Peso: {peso} kg\n"
                              f"Tipo(s): {', '.join(tipos)}")

        imagen_respuesta = requests.get(imagen_url)
        imagen_bytes = io.BytesIO(imagen_respuesta.content)
        imagen_pil = Image.open(imagen_bytes)
        imagen_pil = imagen_pil.resize((150, 150)) 
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk  
    else:
        resultado.config(text="Pokémon no encontrado.")
        etiqueta_imagen.config(image="")

ventana = tk.Tk()
ventana.title("Buscador de Pokémon")
ventana.geometry("400x500")

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Buscar", command=obtener_datos_pokemon)
boton.pack()

resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

ventana.mainloop()
