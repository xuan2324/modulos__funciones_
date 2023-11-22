#Actividad 1 - 25 puntos
#Por consola se piden como máximo 5 números hasta que pulsas q muestra la suma de los números introducidos.
#algoritmo funciona:5 puntos
#algoritmo utiliza mejora en argumentos : 5 puntos
#algoritmo controla errores y excepciones : 5 puntos
#algoritmo aplica funciones anónimas o recursividad : 5 puntos
#algoritmo resuelve una mejora de funcionalidad : 5 puntos
def sumar_numeros(entrada_usuario, suma=0, contador=0):
    try:
        if contador < 5:
            if entrada_usuario.lower() == 'fin':
                return suma
            else:
                numero = float(entrada_usuario)
                suma += numero
                contador += 1

            nueva_entrada = input("Introduce otro número (o 'fin' para salir): ")
            return sumar_numeros(nueva_entrada, suma, contador)
        else:
            print("Has alcanzado el máximo de 5 números.")
            return suma

    except ValueError:
        print("Error: Debes introducir un número válido.")
        return sumar_numeros(input("Vuelve a intentarlo: "), suma, contador)

resultado = sumar_numeros(input("Introduce un número (o 'fin' para salir): "))

print(f"La suma de los números introducidos es: {resultado}")
