from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular

# Carga puntual
c1 = CargaPuntual(posicion=3, magnitud=-500)
c1.mostrar()

# Carga distribuida rectangular
c2 = CargaDistribuidaRectangular(inicio=1, fin=4, intensidad=-300)
c2.mostrar()

# Carga distribuida triangular
c3 = CargaDistribuidaTriangular(inicio=2, fin=5, intensidad_maxima=-250, hacia_derecha=True)
c3.mostrar()

# Triangular en dirección contraria (creciente hacia la izquierda)
c4 = CargaDistribuidaTriangular(inicio=0, fin=3, intensidad_maxima=-200, hacia_derecha=False)
c4.mostrar()
