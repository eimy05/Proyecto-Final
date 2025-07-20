from cargapuntual import CargaPuntual
from cargarectangular import CargaDistribuidaRectangular
from cargatriangular import CargaDistribuidaTriangular
from viga import Viga

viga_1 = Viga(6)

viga_1.agregar_carga(CargaPuntual(2, -400))
viga_1.agregar_carga(CargaDistribuidaRectangular(1, 3, -200))
viga_1.agregar_carga(CargaDistribuidaTriangular(3, 6, -300, hacia_derecha=True))

viga_1.mostrar_cargas()
viga_1.calcular_reacciones()
