# Pregunte al usuario sus colores favoritos, cuando el usuario ingrese "salir" el programa debe terminar de pedir sus colores favoritos.
# Cree una función que imprima en mayúsculas los colores, uno por linea. Utilice kwargs o args según corresponda
from functools import reduce
lista_palabras = []
def colores(lista):
    resultado = reduce(lambda a, b: a + " " + b, lista)
    return resultado

def main():
    colores = input("Ingrese sus colores favoritos sepa:")
    while colores != "salir":
        lista_palabra =lista_palabras.append
    print(lista_palabras) 

if __name__ == '__main__':
    main()
