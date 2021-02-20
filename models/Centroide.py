from .Nodo import Nodo

class Centroide(Nodo):
    def __init__(self, x: int, y: int, name=''):
        super().__init__(x, y)
        self.name = name
        self.nodos = []

    def add_dato(self, dato: Nodo):
        self.nodos.append(dato)

    def get_datos(self):
        return self.nodos

    def clean_data(self):
        self.nodos = []

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return 'class Centroide: X = ' + str(self.x) + ', Y = ' + str(self.y) + ' name = ' + self.name