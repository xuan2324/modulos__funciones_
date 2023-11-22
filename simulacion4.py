#Actividad 4
#Crea un módulo con las siguientes clases
#Mesa
#Silla
#Lampara
#las tres clases tiene como atributo color y precio.
#En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

#algoritmo funciona:5 puntos
#algoritmo utiliza características de POO : 5 puntos
#algoritmo controla errores y excepciones : 5 puntos
#algoritmo aplica enumeradores o similar para Color : 5 puntos
#algoritmo resuelve una mejora de funcionalidad : 5 puntos
from enum import Enum

class Color(Enum):
    AZUL = "Azul"
    ROJO = "Rojo"
    OTRO = "Otro"

class Mesa:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Silla:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Lampara:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

def crear_sillas():
    silla_azul = Silla(Color.AZUL, 9.95)
    silla_roja = Silla(Color.ROJO, 9.95)
    return silla_azul, silla_roja

def main():
    silla_azul, silla_roja = crear_sillas()

    print(f"Silla Azul - Color: {silla_azul.color.value}, Precio: ${silla_azul.precio:.2f}")
    print(f"Silla Roja - Color: {silla_roja.color.value}, Precio: ${silla_roja.precio:.2f}")

if __name__ == "__main__":
    main()
