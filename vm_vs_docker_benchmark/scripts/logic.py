# scripts/logic.py

import random

BOARD_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2]

class Barco:
    def __init__(self, tamaño, coordenadas):
        self.tamaño = tamaño
        self.coordenadas = coordenadas
        self.tocados = set()

    def esta_hundido(self):
        return len(self.tocados) == self.tamaño

    def recibir_disparo(self, coord):
        if coord in self.coordenadas:
            self.tocados.add(coord)
            return True
        return False

class Tablero:
    def __init__(self):
        self.barcos = []
        self.disparos = set()

    def colocar_barcos_aleatoriamente(self):
        for tamaño in SHIP_SIZES:
            while True:
                orientacion = random.choice(['H', 'V'])
                x = random.randint(0, BOARD_SIZE - (tamaño if orientacion == 'H' else 1))
                y = random.randint(0, BOARD_SIZE - (1 if orientacion == 'H' else tamaño))
                coords = [(x+i, y) if orientacion == 'H' else (x, y+i) for i in range(tamaño)]

                if not any(c in pos for barco in self.barcos for pos in barco.coordenadas for c in coords):
                    self.barcos.append(Barco(tamaño, coords))
                    break

    def disparar(self, coord):
        if coord in self.disparos:
            return "Repetido"
        self.disparos.add(coord)
        for barco in self.barcos:
            if barco.recibir_disparo(coord):
                if barco.esta_hundido():
                    return "Hundido"
                return "Tocado"
        return "Agua"

    def todos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.barcos)
