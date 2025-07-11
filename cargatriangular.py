from cargapadre import Carga

class CargaDistribuidaTriangular(Carga):
    def __init__(self, inicio, fin, intensidad_maxima, hacia_derecha=True):
        super().__init__("distribuida_triangular")
        self.inicio = inicio
        self.fin = fin
        self.intensidad_maxima = intensidad_maxima
        self.hacia_derecha = hacia_derecha  # Define la inclinación del triángulo

    def mostrar(self):
        direccion = "↘" if self.hacia_derecha else "↙"
        print(f"Carga triangular ({direccion}) de 0 a {self.intensidad_maxima} N/m entre {self.inicio} m y {self.fin} m")
