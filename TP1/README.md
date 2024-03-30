El programa desarrollado para resolver el trabajo, una vez que se ejecuta, cuenta con una pequeña interacción con el usuario, en el que se le pregunta a éste (tratándolo como si fuera el Señor del Fuego) que batallas quiere pelear, refiriendose a si tiene un set de batallas ya elegido o si desea crear uno nuevo en el momento

1) En caso de querer calcular el resultado de minimizar la suma ponderada de un archivo ya existente, se necesita proveer al programa con la ruta de dicho archivo. Ésta debe ser la ruta completa del archivo, para que no haya errores a la hora de leerlo. 
Algunas consideraciones del archivo provisto: 

        a. Como se menciono previamente, el archivo debe ser provisto con su ruta completa, para evitar errores de lectura.

        b. La primera linea del archivo no debe contener datos numéricos

        c. Cada linea debe tener unicamente los datos de una (1) batalla, dispuestos de la siguiente forma: tiempo,peso.

        d. Por último, los datos del tiempo deben ser números estrictamente mayores a 0, mientras que los datos del peso deben ser números mayores o iguales que 0.

2) Si se desea crear un set de batallas en el momento, hay 2 posibilidades para el Señor del Fuego:
   1. Ingresar manualmente las batallas a pelear, indicando el tiempo tardado y el peso de cada una de ellas
   2. Crear un set de batallas aleatorio, de un tamaño especificado por el usuario. Si este es el caso, los tiempos generados son números aleatorios en el intervalo [1,1000] y los pesos se encuentran en el intervalo [0,1000] (el límite superior para la generación de los números fue elegido de forma arbitraria)