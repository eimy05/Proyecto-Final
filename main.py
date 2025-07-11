from graficos import graficar_cortante, graficar_momento
x = [0, 6, 18, 32]
V = [515, -480, -400, -365] # fuerza cortante
M = [0, 3300, 5110, 0] # momento flector

def mostrar_menu():
    print("\n--- Menú de visualización de la viga ---")
    print("1. Mostrar diagrama de fuerza cortante")
    print("2. Mostrar diagrama de momento flector")
    print("0. Salir")

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
