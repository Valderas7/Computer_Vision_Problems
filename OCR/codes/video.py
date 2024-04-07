# Librerías
import easyocr
import cv2

# La primera vez descarga los modelos para los lenguajes declarados abajo.
# Importante: No todos los lenguajes son compatibles para usar conjuntamente
reader = easyocr.Reader(['es', 'en'], gpu=False)  # Español e inglés

# Rutas del vídeo al que se realiza la inferencia y ruta del vídeo que tendrá el detector aplicado
video_path = 'C:\\Users\\valde\Desktop\OCR\\test\\NY.mp4'
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

# Mientras se capture un 'frame', se realiza la inferencia
while ret:

    # El resultado es una lista para cada texto capturado en el 'frame' con las coordenadas X e Y de los puntos 'Top Left',
    # 'Top Right', 'Bottom Right' y 'Bottom Left'; el texto predicho y la puntuación de confianza de la predicción
    results = reader.readtext(frame, detail=1, paragraph=False)

    # Para mostrar el texto en la imagen original o mostrar los 'bounding boxes' se necesitan las coordenadas del texto. Por lo
    # que es necesario que el parámetro 'detail' de 'readtext' esté a '1'
    for (bbox, text, prob) in results:

        # De las coordenadas de las 'bounding boxes' se extraen las coordenadas X e Y de los puntos 'Top Left', 'Top Right',
        # 'Bottom Right' y 'Bottom Left'. Para cada 'bounding boxes', texto y puntuación de cada texto capturado en 
        # el 'frame'...
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        # Se elimina los caracteres no-ASCII para mostrar el texto limpio en la imagen
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

        # Si la puntuación de confianza es mayor que un umbral de 0.5 se dibuja el 'bounding box' y el texto sobre el 'frame'
        if prob > 0.5:

            # Se dibuja el rectángulo en el 'frame', especificando los puntos 'Top Left' y 'Bottom Right' con el color BGR y
            # el grosor especificados
            cv2.rectangle(frame, tl, br, (0, 255, 0), 2)

            # Se escribe el texto en el 'frame', un poco más arriba respecto a los rectángulos de la 'bounding box' (se resta
            # en 10 puntos el Eje Y de la esquina 'Top Left')
            cv2.putText(frame, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Se escribe el 'frame' en el objeto 'VideoWriter' definido arriba
    out.write(frame)

    # Se captura el vídeo 'frame' por 'frame' y devuelve dos valores
    ret, frame = cap.read()

# Se 'sueltan' los objetos de captura y de guardado de vídeos
cap.release()
out.release()

# Se destruyen todas las ventanas
cv2.destroyAllWindows()