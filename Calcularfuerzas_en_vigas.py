#Crear la clase pa analizar las cargas internas 

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
        self.reaccion_vertical = self.viga.reaccion_vertical
        self.cargas_equivalentes = self.viga.cargas_equivalentes
        self.calcular_momento_en_empotramiento()

    def calcular_momento_en_empotramiento(self):  #El momento en el empotramiento no puede ser cero debido al tipo de "viga" que se plantea, entonces toca calcularlo
        M = 0
        for fuerza, posicion in self.cargas_equivalentes:
            M += fuerza * posicion
        self.momento_en_empotramiento = -M 
        
    def calcular_cortante(self, x):
        V = -self.reaccion_vertical
        for fuerza, posicion in self.cargas_equivalentes:
            if posicion <= x:
                V -= fuerza  # Se suma al final, ya que está a la izquierda
        return round(V, 2)  #Resultado con dos decimales, se puede cambiar esto para mas presición

    def calcular_momento(self, x):
        M = self.momento_en_empotramiento  # Aquí calcula un momento en un punto x cualquiera, el anterior es el del emportramiento
        for fuerza, posicion in self.cargas_equivalentes:
            if posicion >= x:  # Evaluas cargas a la derecha del punto
                brazo = posicion - x
                M += fuerza * brazo
        return round(M, 2)

    def calcular_diagramas(self):
        self.cortante.clear()
        self.momento.clear()

        x = self.viga.longitud
        while x >= 0:
            V = self.calcular_cortante(x)
            M = self.calcular_momento(x)

            self.cortante.append((round(x, 2), V))
            self.momento.append((round(x, 2), M))

            x -= self.precision