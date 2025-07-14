from cargapadre import Carga  # Importa la clase Carga desde el archivo carga.py
from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular

class Viga:
    def __init__(self, longitud):
        self.longitud = longitud #metros
        self.cargas = [] #Se crea una lista vacía donde luego se guardarán las cargas.
        
    def agregar_carga(self, carga): #Método para agregar una carga a la viga
        # if: Verifica si la carga está dentro de los límites de la viga
        if hasattr(carga, 'posicion'):  # Para cargas puntuales
            if carga.posicion < 0 or carga.posicion > self.longitud:
                print("Error: la carga está fuera de la viga.")
                return
        elif hasattr(carga, 'inicio') and hasattr(carga, 'fin'):  # Para cargas distribuidas
            if carga.inicio < 0 or carga.fin > self.longitud:
                print("Error: la carga está fuera de la viga.")
                return
        self.cargas.append(carga) #Agrega la carga a la lista de cargas de la viga
            
    def mostrar_cargas(self): #Método para mostrar las cargas aplicadas a la viga
        if not self.cargas:
            print("No hay cargas aplicadas a la viga.")
        else:
            print("Cargas aplicadas:")
            for carga in self.cargas:
                carga.mostrar()

    def calcular_reacciones(self):
        reaccion_vertical = 0 #Inician en cero las reacciones en el empotramiento
        momento_en_apoyo = 0

        self.cargas_equivalentes = []

        for carga in self.cargas:
            if isinstance(carga, CargaPuntual):
                F = carga.magnitud
                x = carga.posicion

            elif isinstance(carga, CargaDistribuidaRectangular):
                base = carga.fin - carga.inicio
                F = carga.intensidad * base
                x = (carga.inicio + carga.fin) / 2

            elif isinstance(carga, CargaDistribuidaTriangular):
                base = carga.fin - carga.inicio
                F = 0.5 * carga.intensidad_maxima * base
                if carga.hacia_derecha:
                    x = carga.inicio + (2 / 3) * base
                else:
                    x = carga.inicio + (1 / 3) * base
                    
            else:
                print("Tipo de carga no reconocido.")
                continue
            
            self.cargas_equivalentes.append((F, x))

            reaccion_vertical += F
            momento_en_apoyo += F * x

        flecha = "↑" if reaccion_vertical > 0 else ("↓" if reaccion_vertical < 0 else "•")
        print(f"Reacción vertical en el empotramiento: {-reaccion_vertical} N {flecha}")
        
        giro = "↺" if momento_en_apoyo > 0 else ("↻" if momento_en_apoyo < 0 else "•")
        print(f"Momento en el empotramiento: {momento_en_apoyo} {giro} N·m")

        self.reaccion_vertical = reaccion_vertical
        self.momento_en_apoyo = momento_en_apoyo
    





