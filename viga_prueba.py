from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular
from viga import Viga
from Calcularfuerzas_en_vigas import CalculadoraEstructural

# Crear viga de prueba de 5 metros
v = Viga(5)

# Agregar cargas
v.agregar_carga(CargaPuntual(0, 0))                         # Carga puntual
v.agregar_carga(CargaDistribuidaRectangular(0, 0, 0))        # Carga rectangular
v.agregar_carga(CargaDistribuidaTriangular(3, 4, 50))         # Carga triangular

# Calcular reacciones
v.calcular_reacciones()

# Analizar esfuerzos
calc = CalculadoraEstructural(viga=v)
calc.importar_datos_de_reaccion()
calc.calcular_diagramas()

# Imprimir resultados
print("\n--- DIAGRAMA DE CORTANTE ---")
for x, V in calc.cortante:
    print(f"x = {x:.2f} m -> V = {V:.2f} N")

print("\n--- DIAGRAMA DE MOMENTO ---")
for x, M in calc.momento:
    print(f"x = {x:.2f} m -> M = {M:.2f} N·m")
