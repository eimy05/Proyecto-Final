class Carga:
    def __init__(self, tipo):
        #Con el constructor __init__, se crea el atributo de instancia 'tipo'.
        #Cada carga tendrá un tipo específico.
        self.tipo = tipo  # "puntual", "rectangular", "triangular"

    def mostrar(self): #Método para mostrar el tipo de la carga
        print(f"Carga del tipo {self.tipo}")
