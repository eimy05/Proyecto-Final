from Calcularfuerzas_en_vigas import CalculadoraEstructural

def obtener_datos_reales(viga):
    calculadora = CalculadoraEstructural(viga=viga, precision=0.1)
    calculadora.calcular_diagramas()
    return (
        [x for x, _ in calculadora.cortante],
        [v for _, v in calculadora.cortante],
        [m for _, m in calculadora.momento]
    )