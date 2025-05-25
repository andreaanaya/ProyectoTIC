# Usa imagen oficial de Python ligera
FROM python:3.13-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia la carpeta scripts al contenedor
COPY scripts/ ./scripts/

# Cambia al directorio scripts
WORKDIR /app/scripts

# Comando para ejecutar el juego
CMD ["python", "main.py"]