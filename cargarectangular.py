from cargapadre import Carga

class CargaDistribuidaRectangular(Carga):
    def __init__(self, inicio, fin, intensidad):
        super().__init__("distribuida_rectangular")
        self.inicio = inicio      # posición donde empieza
        self.fin = fin            # posición donde termina
        self.intensidad = intensidad  # N/m

    def mostrar(self):
        print(f"Carga distribuida rectangular de {self.intensidad} N/m entre {self.inicio} m y {self.fin} m")
