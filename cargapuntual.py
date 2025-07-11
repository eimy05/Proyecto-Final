from cargapadre import Carga

class CargaPuntual(Carga):
    def __init__(self, posicion, magnitud):
        super().__init__("puntual") #Llama al constructor de la clase padre Carga
        self.posicion = posicion
        self.magnitud = magnitud

    def mostrar(self):
        print(f"Carga puntual de {self.magnitud} N en posición {self.posicion} m")


