# scripts/ai.py

import random

class IA:
    def __init__(self):
        self.disparos_realizados = set()

    def elegir_disparo(self):
        while True:
            coord = (random.randint(0, 9), random.randint(0, 9))
            if coord not in self.disparos_realizados:
                self.disparos_realizados.add(coord)
                return coord
