# Librerías
from ultralytics import YOLO
import cv2

# Carga el modelo entrenado customizado y la imagen a inferir
model_path = 'C:\\Users\\valde\Desktop\YOLOv8_object_detector_demo\\results\\train\weights\\best.pt'
model = YOLO(model_path)

# Ruta de la imagen o 'array' de OpenCV, etc
img_path = 'C:\\Users\\valde\Desktop\YOLOv8_object_detector_demo\\test\\tomate_limon.jpg'
#img_path = cv2.imread(img_path)

# Ejecuta la inferencia en una imagen (se podrían añadir más en el 'array'). La inferencia devuelve una lista
results = model([img_path])

# Para cada inferencia de cada imagen, se dividen cada uno de los objetos de una inferencia
# en variables diferentes, para descomponer los resultados
for result in results:

    # Objeto con las 'bounding boxes' (en caso de detección)
    boxes = result.boxes

    # Objeto con las máscaras de segmentación (en este caso ninguna, se hace detección)
    masks = result.masks

    # Objeto con las poses (en este caso ninguna, se hace detección)
    keypoints = result.keypoints

    # Objeto de probabilidades para clasificación (en este caso ninguna, se hace detección)
    probs = result.probs

    # Muestra los resultados en pantalla
    result.show()

    # Guarda los resultados en local
    result.save(filename='{}_out.jpg'.format(img_path[:-4]))