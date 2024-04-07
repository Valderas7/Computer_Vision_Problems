# YOLOv8 Object Detection Demo
En este repositorio se encuentran las imágenes, archivos y códigos desarrollados para ejecutar el entrenamiento y la inferencia de un modelo `YOLOv8` para realizar modelos de detección de objetos. En este caso se entrena un modelo de detección de comida, aunque los ejemplos de inferencia se centran específicamente en detección de limones.

## Estructura

- **codes**: En esta carpeta están los códigos de entrenamiento e inferencia, tanto de imágenes como de vídeos.
- **dataset**: Aquí se encuentran las carpetas donde se almacena el `dataset` (están vacías) y el archivo de configuración `YAML` usado para el entrenamiento. Solo se han subido para que se sepa la estructura que debe seguir el formato `YOLOv8`.
- **docs**: En este directorio se encuentra el archivo de texto que documenta como debe ser la estructura de los datos para el entrenamiento y que sirve como guía para realizar el proceso de entreno e inferencia del modelo.
- **test**: Imágenes y vídeos de entrada (y de salida) a los que se les realiza la inferencia.
- **train_results**: Aquí se encuentra la carpeta generada tras completarse el proceso de entrenamiento.