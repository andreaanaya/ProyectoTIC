import time
import os
from logic import Tablero
from ai import IA

def imprimir_tablero(tablero, mostrar_barcos=False):
    print("   " + " ".join(str(i) for i in range(10)))
    for y in range(10):
        fila = []
        for x in range(10):
            if (x, y) in tablero.disparos:
                contenido = "X" if any((x, y) in b.coordenadas for b in tablero.barcos) else "O"
            elif mostrar_barcos and any((x, y) in b.coordenadas for b in tablero.barcos):
                contenido = "B"
            else:
                contenido = "."
            fila.append(contenido)
        print(f"{y:2} {' '.join(fila)}")

def leer_coordenada():
    while True:
        try:
            entrada = input("Introduce coordenada (x y): ")
            x, y = map(int, entrada.strip().split())
            if 0 <= x <= 9 and 0 <= y <= 9:
                return (x, y)
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except:
            print("Entrada inválida. Usa formato: x y")

def guardar_tiempo(tiempo, entorno="docker"):
    ruta = os.path.join(os.path.dirname(__file__), "..", "results", f"tiempos_{entorno}.txt")
    with open(ruta, "a") as f:
        f.write(f"{tiempo:.2f} segundos\n")

def main():
    print("=== ¡Bienvenido a Hundir la Flota! ===\n")
    
    start_time = time.time()

    jugador = Tablero()
    ia = Tablero()
    ia_bot = IA()

    jugador.colocar_barcos_aleatoriamente()
    ia.colocar_barcos_aleatoriamente()

    turno = 0
    while True:
        print("\n--- Tu tablero ---")
        imprimir_tablero(jugador, mostrar_barcos=True)
        print("\n--- Tablero enemigo ---")
        imprimir_tablero(ia, mostrar_barcos=False)

        if turno % 2 == 0:
            print("\nTu turno:")
            coord = leer_coordenada()
            resultado = ia.disparar(coord)
            print(f"Resultado: {resultado}")
            if ia.todos_hundidos():
                print("¡Ganaste! Has hundido todos los barcos enemigos.")
                break
        else:
            print("\nTurno de la IA...")
            coord = ia_bot.elegir_disparo()
            resultado = jugador.disparar(coord)
            print(f"La IA disparó a {coord}: {resultado}")
            if jugador.todos_hundidos():
                print("La IA ha ganado. Todos tus barcos han sido hundidos.")
                break

        turno += 1

    end_time = time.time()
    duracion = end_time - start_time
    print(f"\nLa partida duró {duracion:.2f} segundos.")

    # Detección automática si estamos en Docker o no
    entorno = "docker" if os.path.exists("/.dockerenv") else "vm"
    guardar_tiempo(duracion, entorno)

if __name__ == "__main__":
    main()
