import random

Anime_dict = {
            "One piece": "pelicula de accion i para ver con amigos",
            "jujutsu kaisen": "serie d'anime muy conocida por sus personajes",
            "la leyenda de aang": "serie d'anime con super poderes diferentes"
        }

palabra = input("Digita la palabra que quieres aprender")

if palabra in Anime_dict.keys():
    print(Anime_dict[palabra])
else:
    print("Debes escribir correctamente la palabra o inicial en mayuscula")
