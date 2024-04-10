# Deep Learning Problems
En este repositorio se encuentran las imágenes, archivos y códigos desarrollados para ejecutar el entrenamiento y/o la inferencia de distintos problemas de `deep learning` que aún no he visto en el ámbito laboral, para al menos tener una mínima idea práctica sobre ellos

## Estructura

- **Object_Detection**: En esta carpeta se encuentran las imágenes, archivos y códigos desarrollados para ejecutar el entrenamiento y la inferencia de un modelo `YOLOv8` para realizar modelos de detección de objetos. En este caso se entrena un modelo de detección de comida, aunque los ejemplos de inferencia se centran específicamente en detección de limones.
    - **codes**: En esta carpeta están los códigos de entrenamiento e inferencia, tanto de imágenes como de vídeos.
    - **dataset**: Aquí se encuentran las carpetas donde se almacena el `dataset` (están vacías) y el archivo de configuración `YAML` usado para el entrenamiento. Solo se han subido para que se sepa la estructura que debe seguir el formato `YOLOv8`.
    - **docs**: En este directorio se encuentra el archivo de texto que documenta como debe ser la estructura de los datos para el entrenamiento y que sirve como guía para realizar el proceso de entreno e inferencia del modelo.
    - **test**: Imágenes y vídeos de entrada (y de salida) a los que se les realiza la inferencia.
    - **train_results**: Aquí se encuentra la carpeta generada tras completarse el proceso de entrenamiento. <br><br>
- **OCR**: En este directorio se encuentran las imágenes, los vídeos y códigos desarrollados para realizar la inferencia con `EasyOCR` del reconocimiento óptico de caracteres en imágenes y vídeos.
    - **codes**: En esta carpeta están los códigos de inferencia, tanto de imágenes como de vídeos.
    - **test**: Imágenes y vídeos de entrada (y de salida) a los que se les realiza la inferencia.
