# script_malo.py

import os  # Importación no utilizada

def funcion_mala():
    a = 5
    b = 10
    c = a + b  # Variable 'c' nunca se usa

    if a > 0:
        pass  # Bloque vacío

    if b < 20:
        print("b es menor que 20")
    else:
        # ELSE vacío
        pass

    # Comentario inútil
    # TODO: arreglar esto algún día

    print("Resultado:", c)  # 'c' no se usa antes

def otra_funcion():
    for i in range(10):
        break  # Bucle innecesario

    return 42
    return 99  # Código muerto
    return 77  # Código muertosssssss

funcion_mala()
