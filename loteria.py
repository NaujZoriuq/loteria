import random

def generar_numeros_ganadores(cantidad_numeros=6, rango_numeros=(1, 49)):
    return random.sample(range(rango_numeros[0], rango_numeros[1] + 1), cantidad_numeros)

def obtener_numeros_usuario(cantidad_numeros=6, rango_numeros=(1, 49)):
    print(f"Selecciona {cantidad_numeros} números entre {rango_numeros[0]} y {rango_numeros[1]}:")
    numeros_usuario = []

    for _ in range(cantidad_numeros):
        while True:
            try:
                numero = int(input("Ingresa un número: "))
                if rango_numeros[0] <= numero <= rango_numeros[1]:
                    break
                else:
                    print(f"Por favor, ingresa un número entre {rango_numeros[0]} y {rango_numeros[1]}.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        numeros_usuario.append(numero)

    return numeros_usuario

def verificar_ganador(numeros_usuario, numeros_ganadores):
    aciertos = set(numeros_usuario) & set(numeros_ganadores)
    return aciertos

def jugar_loteria():
    print("¡Bienvenido al juego de lotería!")

    numeros_ganadores = generar_numeros_ganadores()
    numeros_usuario = obtener_numeros_usuario()

    print(f"\nNúmeros ganadores: {numeros_ganadores}")
    print(f"Tus números: {numeros_usuario}")

    aciertos = verificar_ganador(numeros_usuario, numeros_ganadores)

    if aciertos:
        print(f"\n¡Felicidades! Has acertado en {len(aciertos)} número(s): {aciertos}")
    else:
        print("\nLo siento, no has acertado en ningún número. ¡Mejor suerte la próxima vez!")

if __name__ == "__main__":
    jugar_loteria()