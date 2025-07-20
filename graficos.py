import matplotlib
matplotlib.use('TkAgg')  # ¡Esta línea debe ir ANTES de importar pyplot!
import matplotlib.pyplot as plt

def graficar_diagramas(x, V, M, longitud_viga):
    try:
        # Configuración de la figura
        plt.figure(figsize=(10, 8))
        
        # Diagrama de cortante
        plt.subplot(2, 1, 1)
        plt.plot(x, V, 'b-', linewidth=2)
        plt.fill_between(x, V, color='blue', alpha=0.2)
        plt.title("DIAGRAMA DE FUERZA CORTANTE", fontweight='bold')
        plt.grid(True, linestyle='--')
        plt.axhline(0, color='black', linewidth=1)
        
        # Diagrama de momento
        plt.subplot(2, 1, 2)
        plt.plot(x, M, 'r-', linewidth=2)
        plt.fill_between(x, M, color='red', alpha=0.2)
        plt.title("DIAGRAMA DE MOMENTO FLECTOR", fontweight='bold')
        plt.grid(True, linestyle='--')
        plt.axhline(0, color='black', linewidth=1)
        
        plt.tight_layout()
        plt.show(block=True)  # Bloquea la ejecución hasta cerrar la ventana
        plt.close()  # Libera memoria
    except Exception as e:
        print(f"Error al graficar: {str(e)}")