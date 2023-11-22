#Actividad 2
#En consola se piden las unidades y el precio.
#Estos datos permiten calcular el subtotal.
#Si el día de hoy es anterior al 15 de cada mes, se aplica un descuento del 5%
#Muestra el resultado el total de la factura.
#algoritmo funciona:5 puntos
#algoritmo utiliza mejora en argumentos : 5 puntos
#algoritmo controla errores y excepciones : 5 puntos
#algoritmo aplica funciones anónimas o recursividad : 5 puntos
#algoritmo resuelve una mejora de funcionalidad : 5 puntos
import datetime

def calcular_descuento(subtotal, fecha_actual):
    # Función anónima para aplicar el descuento del 5% si hoy es anterior al día 15
    aplicar_descuento = lambda x: x * 0.95 if fecha_actual.day < 15 else x
    return aplicar_descuento(subtotal)

def obtener_fecha_actual():
    return datetime.datetime.now()

def obtener_valor_numerico(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        print("Error: Debes introducir un valor numérico.")
        return obtener_valor_numerico(mensaje)

def main():
    try:
        unidades = obtener_valor_numerico("Introduce la cantidad de unidades: ")
        precio = obtener_valor_numerico("Introduce el precio por unidad: ")

        subtotal = unidades * precio
        fecha_actual = obtener_fecha_actual()
        total_con_descuento = calcular_descuento(subtotal, fecha_actual)

        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Total con descuento: ${total_con_descuento:.2f}")

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
