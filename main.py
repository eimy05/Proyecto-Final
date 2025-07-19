from calculos import obtener_resultados
from graficos import graficar_cortante, graficar_momento

# Aquí se actualizan los datos manualmente o desde Salomé
posiciones = [0, 2, 4]  # en metros
fuerzas = [100, -300, 10]  # en Newtons

print("Posiciones:", posiciones)
print("Fuerzas:", fuerzas)

# El código genera automáticamente los valores V(x) y M(x)
x, V, M = obtener_resultados(posiciones, fuerzas)

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
        print("Opción no válida, Intente de nuevo.")

print(f"Fuerza total: {sum(fuerzas)} N")
print(f"Momento final: {round(M[-1], 2)} N·m")
