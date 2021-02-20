class Nodo:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return 'class Nodo: X = ' + str(self.x) + ', Y = ' + str(self.y)

    @staticmethod
    def distance(nodo1, nodo2) -> float:
        return ((nodo2.x-nodo1.x)**2 + (nodo2.y-nodo1.y)**2)**0.5
