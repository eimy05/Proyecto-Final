#Crear la clase pa analizar las cargas internas 
from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular

class CalculadoraEstructural:
    def __init__(self, viga, precision=0.1):
        self.viga = viga
        self.precision = precision
        self.reaccion_vertical = 0
        self.precision = precision
        self.reaccion_vertical = 0
        self.momento_en_empotramiento = 0
        self.cortante = []
        self.momento = []
        
        # Verificar y calcular reacciones primero
        if not hasattr(self.viga, 'reaccion_vertical'):
            self.viga.calcular_reacciones()
        
        # Importar datos de la viga
        self.importar_datos_de_reaccion()
        
    def importar_datos_de_reaccion(self):
        self.reaccion_vertical = self.viga.reaccion_vertical
        self.momento_en_empotramiento = self.viga.momento_en_apoyo
        self.cargas_equivalentes = getattr(self.viga, 'cargas_equivalentes', [])
        
        dist_fins = []
        for carga in self.viga.cargas:
            if isinstance(carga, (CargaDistribuidaRectangular, CargaDistribuidaTriangular)):
                dist_fins.append(carga.fin)
        self.fin_max = max(dist_fins) if dist_fins else 0

    def calcular_cortante(self, x):
        V = self.reaccion_vertical  # Fuerza de reaccion en empotramiento
        
        for carga in self.viga.cargas:    ##Definir calculos por tipo de carga
            if isinstance(carga, CargaPuntual):
                if carga.posicion <= x:
                    V -= carga.magnitud  
                    
            elif isinstance(carga, CargaDistribuidaRectangular):
                if x >= carga.inicio:
                    if x <= carga.fin:
                        contribucion = carga.intensidad * (x - carga.inicio)
                    else:
                        contribucion = carga.intensidad * (carga.fin - carga.inicio)
                    V -= contribucion
                    
            elif isinstance(carga, CargaDistribuidaTriangular):
                base_total = carga.fin - carga.inicio
                if base_total == 0 or carga.intensidad_maxima == 0:
                    continue  # De esta forma, si no hay una carga triangular, no ocurrira un error por dividir entre cero

                if x >= carga.inicio and  x <= carga.fin:
                    base_activa = x - carga.inicio
                else:
                        base_activa = base_total
                    
                    if carga.hacia_derecha:
                        intensidad = carga.intensidad_maxima * (base_activa / base_total)
                    else:
                        intensidad = carga.intensidad_maxima * (1 - (base_activa / base_total))
                    
                    contribucion = 0.5 * intensidad * base_activa
                    V -= contribucion
        
        return round(V, 2)

    def calcular_momento(self, x):
        M = 0
    
        M += self.reaccion_vertical * x
    
        M -= self.momento_en_empotramiento
    
        # calculo de momento por cargas
        for carga in self.viga.cargas:
            if isinstance(carga, CargaPuntual) and carga.posicion <= x:
                M -= carga.magnitud * (x - carga.posicion)
            
            elif isinstance(carga, CargaDistribuidaRectangular):
                x_inicio = max(carga.inicio, 0)
                x_fin = min(carga.fin, x)
            
                if x_fin > x_inicio:
                    fuerza = carga.intensidad * (x_fin - x_inicio)
                    centroide = x_inicio + (x_fin - x_inicio)/2
                    M -= fuerza * (x - centroide)
                
            elif isinstance(carga, CargaDistribuidaTriangular):
                x_inicio = max(carga.inicio, 0)
                x_fin = min(carga.fin, x)
            
                if x_fin > x_inicio:
                    base = x_fin - x_inicio
                    if carga.hacia_derecha:
                        centroide = x_inicio + (1/3)*base
                        intensidad = carga.intensidad_maxima * (base/(carga.fin - carga.inicio))
                    else:
                        centroide = x_inicio + (2/3)*base
                        intensidad = carga.intensidad_maxima * (1 - base/(carga.fin - carga.inicio))
                
                    M -= 0.5 * intensidad * base * (x - centroide)
    
        return round(M, 2)

    def calcular_diagramas(self):  ## definir los diagramas
        self.cortante = []
        self.momento = []
        
        x = 0
        while x <= self.viga.longitud + self.precision/2:  
            V = self.calcular_cortante(x)
            M = self.calcular_momento(x)
            
            self.cortante.append((round(x, 2), V))
            self.momento.append((round(x, 2), M))
            
            x += self.precision