import algoritmo
import matplotlib.pyplot as plt


RUTA_10 = "archivos/10.txt"
RUTA_50 = "archivos/50.txt"
RUTA_100 = "archivos/100.txt"
RUTA_1000 = "archivos/1000.txt"
RUTA_5000 = "archivos/5000.txt"
RUTA_10000 = "archivos/10000.txt"
RUTA_100000 = "archivos/100000.txt"

tiempos = []
#tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_10))[2])
#tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_50))[2])
#tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_100))[2])
#tiempos.append(algoritmo.minimizar_suma(algoritmo.generar_batallas_random(500))[2])
#tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_1000))[2])
#tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_5000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_10000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.generar_batallas_random(50000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.leer_archivo(RUTA_100000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.generar_batallas_random(500000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.generar_batallas_random(1000000))[2])
tiempos.append(algoritmo.minimizar_suma(algoritmo.generar_batallas_random(10000000))[2])
valores = [10000,50000,100000,500000,1000000,10000000]
#valores = [10,50,100,500,1000]#,5000,10000,50000,100000,500000,1000000]
tabla = []
tabla.append(valores)
tabla.append(tiempos)
print(tiempos)

plt.plot(tabla[0], tabla[1])
plt.show()