# Librerías
from ultralytics import YOLO
import cv2

# Rutas del vídeo al que se realiza la inferencia y ruta del vídeo que tendrá el detector aplicado
video_path = 'C:\\Users\\valde\Desktop\YOLOv8_object_detector_demo\\test\\limones.mp4'
video_path_out = '{}_out.mp4'.format(video_path[:-4])

# Se define un objeto para captura de vídeo con la ruta donde se encuentra el archivo de vídeo
cap = cv2.VideoCapture(video_path)

# El método 'read' captura el vídeo frame por frame y devuelve dos valores
# ret: Esta variable booleana es True cuando SÍ se ha capturado una imagen, mientras que es False cuando NO
# frame: Es la imagen con la cual se puede trabajar.
ret, frame = cap.read()

# Altura (H), anchura (W) y canales de la imagen
H, W, _ = frame.shape

# Se crea un objeto para guardar un video en el 'path' de salida usando el codec de 4 caracteres usado para comprimir los
# frames (fourcc) y especificando el ratio de frames del video (FPS) con la altura y anchura del frame (framesize)
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Carga el modelo entrenado customizado
model_path = 'C:\\Users\\valde\Desktop\YOLOv8_object_detector_demo\\train_results\\train\weights\\best.pt'
model = YOLO(model_path)

# Umbral
threshold = 0.5

# Mientras se capture un 'frame', se realiza la inferencia
while ret:
    results = model(frame)[0]

    # Para la inferencia de cada 'frame', se subdivide cada lista, que representa una 'bounding box', en varias variables
    for result in results.boxes.data.tolist():

        # Coordenadas X e Y de las esquinas 'Top Left' y 'Bottom Right' de la 'bounding box', probabilidad de la clase y
        # número entero que representa a dicha clase
        x1, y1, x2, y2, score, class_id = result

        # Si la probabilidad de la clase es mayor que el umbral establecido se dibuja un rectángulo en el 'frame' en la
        # posición de las esquinas 'Top Left' y 'Bottom Right' y se escribe en texto la clase a la que pertenece
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Se escribe el 'frame' en el objeto 'VideoWriter' definido arriba
    out.write(frame)

    # Se captura el vídeo frame por frame y devuelve dos valores
    ret, frame = cap.read()

# Se 'sueltan' los objetos de captura y de guardado de vídeos
cap.release()
out.release()

# Se destruyen todas las ventanas
cv2.destroyAllWindows()

# Alternativa
# Inferencia directamente con la ruta del vídeo
#results = model(video_path, stream=True)

# Para la inferencia de cada 'frame', se subdivide cada lista, que representa una 'bounding box', en varias variables
#for result in results:
    #print(result.boxes.data.tolist()) # Imprime las coordenadas, la puntuación y la clase, por lo que habría que extraerlas