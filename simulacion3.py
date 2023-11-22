#Actividad 3
#En consola pides número inicial.
#En consola pides número final.
#Muestra una lista con todos los números pares que hay entre estos dos números.
#algoritmo funciona:5 puntos
#algoritmo utiliza mejora en argumentos : 5 puntos
#algoritmo controla errores y excepciones : 5 puntos
#algoritmo aplica funciones anónimas o recursividad : 5 puntos
#algoritmo resuelve una mejora de funcionalidad : 5 puntos
def mostrar_numeros(inicial, final, paso=1):
    # Función anónima para verificar la dirección del paso
    paso_func = (lambda x: range(inicial, final + 1, paso)) if paso > 0 else (lambda x: range(inicial, final - 1, paso))

    # Utiliza la función anónima para obtener la secuencia de números
    numeros = paso_func(0)

    # Muestra los números
    for numero in numeros:
        print(numero, end=" ")

def obtener_valor_numerico(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: Debes introducir un valor numérico.")
        return obtener_valor_numerico(mensaje)

def main():
    try:
        inicio = obtener_valor_numerico("Introduce el número inicial: ")
        fin = obtener_valor_numerico("Introduce el número final: ")
        paso = obtener_valor_numerico("Introduce el paso (opcional, presiona Enter para usar 1): ") or 1

        mostrar_numeros(inicio, fin, paso)

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
