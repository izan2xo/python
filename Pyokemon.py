import requests

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos["name"].capitalize()
        id_pokemon = datos["id"]
        altura = datos["height"] / 10  # Convertir a metros
        peso = datos["weight"] / 10  # Convertir a kg
        tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]

        print(f"\nNombre: {nombre}")
        print(f"ID: {id_pokemon}")
        print(f"Altura: {altura} m")
        print(f"Peso: {peso} kg")
        print(f"Tipo(s): {', '.join(tipos)}")
    else:
        print("Pokémon no encontrado. Verifica el nombre.")

if __name__ == "__main__":
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
    obtener_datos_pokemon(nombre_pokemon)
