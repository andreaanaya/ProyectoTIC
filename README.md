# Hundir la Flota - Proyecto Final

**Lenguaje:** Python

---

## Introducción

Este proyecto consiste en desarrollar un juego clásico de **Hundir la Flota** para comparar su rendimiento en dos entornos distintos:  
- **Máquina Virtual (Ubuntu)**  
- **Docker**

Se ha implementado la lógica del juego, un modo de interacción por consola, y se registran los tiempos de ejecución para analizar cuál entorno ofrece mejor rendimiento.  

El repositorio incluye:  
- Código fuente en la carpeta `scripts/`  
- Scripts de análisis en `notebooks/`  
- Resultados y logs en `results/`  

---
🛠️ ## Estructura del Proyecto
scripts/: Contiene el código fuente del juego y scripts auxiliares.

notebooks/: Análisis y visualización de los resultados.

results/: Resultados obtenidos de las pruebas de rendimiento.

Dockerfile: Configuración para el contenedor Docker.

requirements.txt: Dependencias necesarias para el proyecto.
## 🧱 Estructura del Proyecto

<pre> ProyectoTIC/
├── README.md
├── scripts/
│   ├── hundir_la_flota.py
│   ├── comparar_tiempos.py
│   ├── docker_setup.sh
│   └── vm_setup.sh
├── notebooks/
│   └── analisis_benchmark.ipynb
├── results/
│   ├── benchmark_vm.csv
│   ├── benchmark_docker.csv
│   ├── grafica_cpu.png
│   ├── grafica_ram.png
│   └── grafica_tiempo.png
├── Dockerfile
└── requirements.txt</pre>

## Para ponerlo en marcha...

1. Ejecutar el juego en la VM con Ubuntu.  
2. Ejecutar el juego dentro del contenedor Docker.  
3. Comparar tiempos con el script `comparar_tiempos.py`.  

<pre> 
---

## ⚙️ Tecnologías Usadas

- Python 3.10
- Docker
- VirtualBox
- Flask (opcional si añades interfaz)
- psutil, pandas, matplotlib

---

## 📦 Instalación de Dependencias

```bash
pip install -r requirements.txt</pre>
---

¡Gracias por visitar el proyecto!
