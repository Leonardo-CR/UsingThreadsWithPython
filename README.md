# Descarga de Imágenes en Paralelo con Python

Este proyecto de Python permite descargar múltiples imágenes desde una lista de URLs utilizando **hilos (threads)** para realizar las descargas en paralelo. Esto reduce significativamente el tiempo total de descarga en comparación con un enfoque secuencial.

## 📂 Estructura del proyecto

- Threads.py (ejemplo de descarga sin uso de hilos)
- ThreadsTrue.py (descarga con uso de hilos)


## 🚀 Tecnologías utilizadas

- Python 3
- Módulos estándar:
  - `os`
  - `urllib.request`
  - `concurrent.futures`
  - `time`

## 🧠 ¿Qué hace el script?

1. **Define una lista de URLs** que apuntan a imágenes en línea.
2. **Crea una carpeta local** para guardar las imágenes descargadas (`Threads/imagenesHilos`).
3. **Usa `ThreadPoolExecutor`** para descargar imágenes en paralelo.
4. **Mide el tiempo total de ejecución** para mostrar la mejora en rendimiento.
5. **Imprime resultados** de cada descarga (éxito o fallo).

## 🔧 Cómo usar

1. Asegúrate de tener Python 3 instalado.
2. Copia el código a un archivo, por ejemplo, `descargar_imagenes.py`.
3. Ejecuta el script:

```bash
python descargar_imagenes.py
