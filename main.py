from viga import Viga
from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular
from calculos import obtener_datos_reales
from graficos import graficar_diagramas

def ingresar_cargas(viga):
    while True:
        print("\n🔹 Tipos de carga:")
        print("1. Carga puntual")
        print("2. Carga rectangular")
        print("3. Carga triangular")
        print("0. Terminar y graficar")
        
        opcion = input("Seleccione el tipo de carga (o 0 para finalizar): ")
        
        if opcion == "1":
            posicion = float(input("Posición (m, medido desde la izquierda): "))
            magnitud = float(input("Magnitud (N, positivo hacia abajo): "))
            viga.agregar_carga(CargaPuntual(posicion, -magnitud))
        
        elif opcion == "2":
            inicio = float(input("Inicio (m): "))
            fin = float(input("Fin (m): "))
            intensidad = float(input("Intensidad (N/m, positivo hacia abajo): "))
            viga.agregar_carga(CargaDistribuidaRectangular(inicio, fin, -intensidad))
        
        elif opcion == "3":
            inicio = float(input("Inicio (m): "))
            fin = float(input("Fin (m): "))
            intensidad_max = float(input("Intensidad máxima (N/m, positivo hacia abajo): "))
            direccion = input("Dirección (derecha/izquierda): ").lower()
            hacia_derecha = direccion == "derecha"
            viga.agregar_carga(CargaDistribuidaTriangular(inicio, fin, -intensidad_max, hacia_derecha))
        
        elif opcion == "0":
            break
        
        else:
            print("❌ Opción no válida.")

def main():
    print("📏 === CALCULADORA DE VIGAS ===")
    longitud = float(input("Longitud de la viga (m): "))
    viga = Viga(longitud)
    
    ingresar_cargas(viga)
    viga.mostrar_cargas()
    
    x, V, M = obtener_datos_reales(viga)
    print("\nDatos para graficar:")
    print("Posiciones:", x)
    print("Cortante:", V)
    print("Momento:", M)
    
    graficar_diagramas(x, V, M, viga.longitud)

if __name__ == "__main__":
    main()