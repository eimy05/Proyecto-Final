from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular
from viga import Viga
from Calcularfuerzas_en_vigas import CalculadoraEstructural

def probar_viga():
    # Crear viga de prueba de 5 metros
    v = Viga(5)

    # Agregar cargas de prueba (puedes modificar estos valores)
    print("\n=== CONFIGURACIÓN DE CARGA ===")
    v.agregar_carga(CargaPuntual(3, 10))  # Carga puntual de 10 N a 3m
    v.agregar_carga(CargaDistribuidaRectangular(0, 0, 0))  # Carga rectangular 5 N/m entre 1m-4m
    v.agregar_carga(CargaDistribuidaTriangular(0, 0, 0, True))  # Carga triangular ↗ 0-8 N/m entre 2m-5m

    # Mostrar configuración de cargas
    v.mostrar_cargas()

    # Calcular reacciones
    v.calcular_reacciones()

    # Calcular diagramas
    calc = CalculadoraEstructural(viga=v, precision=0.5)  # Mayor precisión para pruebas
    calc.calcular_diagramas()

    # Imprimir resultados en formato tabla
    print("\n=== RESULTADOS ===")
    print("\n--- DIAGRAMA DE CORTANTE ---")
    print(f"{'Posición (m)':<15} {'Cortante (N)':<15} {'Gráfico':<10}")
    print("-" * 45)
    for x, V in calc.cortante:
        flecha = "↑" if V < 0 else ("↓" if V > 0 else "•")
        barra = "█" * int(abs(V)/2) if V != 0 else ""
        print(f"{x:<15.2f} {V:<15.2f} {flecha} {barra}")

    print("\n--- DIAGRAMA DE MOMENTO ---")
    print(f"{'Posición (m)':<15} {'Momento (N·m)':<15} {'Gráfico':<10}")
    print("-" * 45)
    for x, M in calc.momento:
        giro = "↺" if M > 0 else ("↻" if M < 0 else "•")
        barra = "█" * int(abs(M)) if M != 0 else ""
        print(f"{x:<15.2f} {M:<15.2f} {giro} {barra}")

    # Puntos críticos adicionales
    print("\n=== PUNTOS CRÍTICOS ===")
    print(f"• Cortante máximo: {max(abs(V) for _, V in calc.cortante):.2f} N")
    print(f"• Momento máximo: {max(abs(M) for _, M in calc.momento):.2f} N·m")

if __name__ == "__main__":
    probar_viga()