import matplotlib.pyplot as plt
import random
from models.Nodo import Nodo
from models.Centroide import Centroide

NODOS_TO_GENERATE = 1000
CENTROIDES_TO_GENERATE = 10
TOLERANCE = 0.01
nodos = []
centroides = []
error = 1


def shorter_distance(arrayDistances) -> float:
    index = 0
    dist = arrayDistances[0]['distance']

    for dictionary in arrayDistances:
        if dictionary['distance'] < dist:
            dist = dictionary['distance']
            index = dictionary['index']

    return index, dist


def mean_x(datos: [Nodo]) -> float:
    suma = 0

    for nodo in datos:
        suma += nodo.x

    return suma / len(datos)


def mean_y(datos: [Nodo]) -> float:
    suma = 0
    for nodo in datos:
        suma += nodo.y

    return suma / len(datos)


def generar_color():
    values = ['0', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    n = '#'
    for _ in range(6):
        n = n + random.choice(values)
    return n


if __name__ == "__main__":
    '''
        Generar datos al azar
    '''
    for _ in range(NODOS_TO_GENERATE):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        nodos.append(Nodo(x, y))

    for count in range(CENTROIDES_TO_GENERATE):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        centroides.append(Centroide(x, y, 'Centroide: ' + str(count + 1)))

    '''
        Calculo de error
    '''
    while error > TOLERANCE:
        [centroide.clean_data() for centroide in centroides]

        for nodo in nodos:
            distancias = []

            for index, centro in enumerate(centroides):
                datoAux = {
                    'index': index,
                    'distance': Nodo.distance(nodo, centro)
                }

                distancias.append(datoAux)

            index, _ = shorter_distance(distancias)

            centroides[index].add_dato(nodo)

        errores = []

        for centroide in centroides:
            old_x = centroide.x
            old_y = centroide.y

            centroide_datos = centroide.get_datos()
            centroide.move(mean_x(centroide_datos), mean_y(centroide_datos))

            new_x = centroide.x
            new_y = centroide.y

            errores.append(abs(old_x - new_x))

        error = max(errores)

    '''
        Graficar
    '''
    for centroide in centroides:
        array_x = []
        array_y = []

        for nodo in centroide.get_datos():
            array_x.append(nodo.x)
            array_y.append(nodo.y)

        plt.scatter(centroide.x, centroide.y, c=[generar_color()], marker="*")
        plt.text(centroide.x + .03, centroide.y + .03,
                 centroide.name, fontsize=9)

        plt.scatter(array_x, array_y, c=generar_color())

    plt.show()
