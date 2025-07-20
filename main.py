from graficos import graficar_cortante, graficar_momento
from calculos import obtener_datos_de_salome

def mostrar_menu():
    print("\n--- Menú de visualización de la viga ---")
    print("1. Mostrar diagrama de fuerza cortante")
    print("2. Mostrar diagrama de momento flector")
    print("0. Salir")

# Obtener datos actualizados desde Salomé
x, V, M = obtener_datos_de_salome()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        graficar_cortante(x, V)
    elif opcion == "2":
        graficar_momento(x, M)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
