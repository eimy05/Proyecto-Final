import matplotlib.pyplot as plt

def graficar_cortante(x, V):
    plt.figure()
    plt.plot(x, V, color='red', linewidth=2)
    plt.title("Diagrama de Fuerza Cortante")
    plt.xlabel("Longitud de la viga (m)")
    plt.ylabel("Fuerza cortante (N)")
    plt.grid(True)
    plt.axhline(0, color='black', linestyle='--')
    plt.show()

def graficar_momento(x, M):
    plt.figure()
    plt.plot(x, M, color='blue', linewidth=2)
    plt.title("Diagrama de Momento Flector")
    plt.xlabel("Longitud de la viga (m)")
    plt.ylabel("Momento flector (N·m)")
    plt.grid(True)
    plt.axhline(0, color='black', linestyle='--')
    plt.show()
