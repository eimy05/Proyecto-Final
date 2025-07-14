from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular
from viga import Viga
from Calcularfuerzas_en_vigas import CalculadoraEstructural

# Crear viga de prueba de 5 metros
v = Viga(5)

# Agregar cargas
#Nota: La posición se mide de izquierda a derecha, y las cargas positivas indican fuerzas hacia abajo.
#Un momento positivo indica un giro en sentido antihorario.
v.agregar_carga(CargaPuntual(0, 0))                         #Carga puntual (posición, magnitud)
v.agregar_carga(CargaDistribuidaRectangular(0, 0, 0))         #Carga rectangular(inicio, fin, magnitud en N/m)
v.agregar_carga(CargaDistribuidaTriangular(0, 0, 0, True))    # Carga triangular (inicio, fin, magnitud max en N/m, True=⬊)

# Calcular reacciones
v.calcular_reacciones()

# Calcular fuerza cortante y momento
calc = CalculadoraEstructural(viga=v)
calc.importar_datos_de_reaccion()
calc.calcular_diagramas()

# Imprimir resultados
print("\n--- DIAGRAMA DE CORTANTE ---")
for x, V in calc.cortante:
    print(f"x = {x:.2f} m -> V = {V:.2f} N")

print("\n--- DIAGRAMA DE MOMENTO ---")
for x, M in calc.momento:
    giro = "↺" if M > 0 else ("↻" if M < 0 else "•")
    print(f"x = {x:.2f} m -> M = {M:.2f} N·m {giro}")

