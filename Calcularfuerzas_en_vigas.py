#Crear la clase pa analizar las cargas internas 
from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular

class CalculadoraEstructural:
    def __init__(self, viga, precision=0.1):
        self.viga = viga
        self.precision = precision #El calculo se hará con pasos de 0.1
        self.reaccion_vertical = None
        self.cargas_equivalentes = []
        self.momento_en_empotramiento = 0
        self.cortante = []
        self.momento = []

    def importar_datos_de_reaccion(self):    #Importar las clases de cargas y viga
        self.reaccion_vertical = -self.viga.reaccion_vertical
        self.cargas_equivalentes = self.viga.cargas_equivalentes
        self.momento_en_empotramiento = -self.viga.momento_en_apoyo
        
        dist_fins = [
            carga.fin
            for carga in self.viga.cargas
            if isinstance(carga, (CargaDistribuidaRectangular, CargaDistribuidaTriangular))
        ]
        self.fin_max = max(dist_fins) if dist_fins else 0

        self.usar_integracion = any(
        isinstance(c, (CargaDistribuidaRectangular, CargaDistribuidaTriangular))
        for c in self.viga.cargas
        )

    def calcular_momento_en_empotramiento(self):  #El momento en el empotramiento no puede ser cero debido al tipo de "viga" que se plantea, entonces toca calcularlo
        M = 0
        for fuerza, posicion in self.cargas_equivalentes:
            M += fuerza * posicion
        self.momento_en_empotramiento = -M 
        
    def calcular_cortante(self, x):
        V = -self.reaccion_vertical

        for carga in self.viga.cargas:
            if isinstance(carga, CargaPuntual):  #Pa que calcule correctamente no solo la puntual toca ir carga por carga
                if carga.posicion <= x:
                    V -= carga.magnitud

            elif isinstance(carga, CargaDistribuidaRectangular):
                if x >= carga.inicio:
                    if x <= carga.fin:
                        largo_activo = x - carga.inicio  #si no se pone asi, no se verá reflejado la forma correcta de la grafica ya que calculara mal la cortante donde se  haga el corte
                    else:
                        largo_activo = carga.fin - carga.inicio
                    V -= carga.intensidad * largo_activo

            elif isinstance(carga, CargaDistribuidaTriangular):
                base_total = carga.fin - carga.inicio
                if base_total == 0 or carga.intensidad_maxima == 0:
                    continue  # De esta forma, si no hay una carga triangular, no ocurrira un error por dividir entre cero

                if x >= carga.inicio and  x <= carga.fin:
                    base_activa = x - carga.inicio
                else:
                        base_activa = base_total

                altura = (
                        carga.intensidad_maxima * (base_activa / base_total)
                    if carga.hacia_derecha
                    else carga.intensidad_maxima * (1 - (base_activa / base_total))
                )

                F = 0.5 * altura * base_activa
                V -= F

        return round(V, 2)


    def calcular_momento(self, x):
        if x >= self.pos_max_carga:
            return 0.0
        
        M = self.momento_en_empotramiento  # Aquí calcula un momento en un punto x cualquiera, el anterior es el del emportramiento
        M -= self.reaccion_vertical * x
        for fuerza, posicion in self.cargas_equivalentes:
            if posicion <= x:  # Evaluas cargas a la derecha del punto
                brazo = x - posicion
                M -= fuerza * brazo
        return round(M, 2)

    def calcular_diagramas(self):
        self.cortante.clear()
        self.momento.clear()

        # Paso 1: punto inicial
        x = 0.0
        V_prev = self.calcular_cortante(x)
        self.cortante.append((round(x, 2), V_prev))

        if self.usar_integracion:
            M = self.momento_en_empotramiento
            self.momento.append((round(x, 2), round(M, 2)))

            # Paso 2: integración trapezoidal
            x += self.precision
            while round(x, 5) <= self.viga.longitud:
                V_curr = self.calcular_cortante(x)

                if x <= self.fin_max:
                    # trapezoide: area entre V_prev y V_curr
                    M = M + (V_prev + V_curr) / 2 * self.precision
                    # no permitimos M > 0
                    if M > 0:
                        M = 0.0
                else:
                    M = 0.0

                self.cortante.append((round(x, 2), V_curr))
                self.momento.append((round(x, 2), round(M, 2)))

            
                V_prev = V_curr
                x += self.precision

        else:
            # tu bucle original para cargas puntuales
            while round(x, 5) <= self.viga.longitud:
                V = self.calcular_cortante(x)
                M = self.calcular_momento(x)

                self.cortante.append((round(x, 2), V))
                self.momento.append((round(x, 2), M))
                x += self.precision

