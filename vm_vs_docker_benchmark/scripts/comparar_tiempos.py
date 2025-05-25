import os
from datetime import datetime

def leer_tiempos(path):
    tiempos = []
    if os.path.exists(path):
        with open(path, "r") as f:
            for linea in f:
                try:
                    tiempo = float(linea.strip().split()[0])
                    tiempos.append(tiempo)
                except:
                    continue
    return tiempos

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0.0

def main():
    base_dir = os.path.dirname(__file__)
    resultados_dir = os.path.abspath(os.path.join(base_dir, "..", "results"))

    docker_file = os.path.join(resultados_dir, "tiempos_docker.txt")
    vm_file = os.path.join(resultados_dir, "tiempos_vm.txt")
    salida_file = os.path.join(resultados_dir, "comparacion.txt")

    tiempos_docker = leer_tiempos(docker_file)
    tiempos_vm = leer_tiempos(vm_file)

    prom_docker = promedio(tiempos_docker)
    prom_vm = promedio(tiempos_vm)
    diferencia = prom_vm - prom_docker

    resultado = [
        "=== Comparación de Tiempos ===",
        f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Partidas en Docker: {len(tiempos_docker)}",
        f"Partidas en VM:     {len(tiempos_vm)}",
        f"Promedio en Docker: {prom_docker:.2f} segundos",
        f"Promedio en VM:     {prom_vm:.2f} segundos",
    ]

    if diferencia > 0:
        resultado.append(f"Docker fue más rápido por {abs(diferencia):.2f} segundos.")
    elif diferencia < 0:
        resultado.append(f"La VM fue más rápida por {abs(diferencia):.2f} segundos.")
    else:
        resultado.append("Ambos entornos fueron igual de rápidos.")

    print("\n".join(resultado))

    # Guardar en archivo
    with open(salida_file, "a") as f:
        f.write("\n".join(resultado) + "\n\n")

if __name__ == "__main__":
    main()
