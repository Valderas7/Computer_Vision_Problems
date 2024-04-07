# Librerías
import easyocr
import cv2

# La primera vez descarga los modelos para los lenguajes declarados abajo.
# Importante: No todos los lenguajes son compatibles para usar conjuntamente
reader = easyocr.Reader(['es', 'en'], gpu=False)  # Español e inglés

# Imagen a inferir
img_path = 'C:\\Users\\valde\Desktop\OCR\\test\\ej1.jpg'
img = cv2.imread(img_path)

# Método principal para leer texto sobre la imagen. El parámetro 'detail' indica si la salida de texto se quiere con detalles
# o no; y el parámetro 'Paragraph' combina los resultados, pudiendolos capturar en un 'dataframe' fácilemente si es True.
# El resultado es una lista para cada texto capturado en la imagen con las coordenadas X e Y de los puntos 'Top Left', 
# 'Top Right', 'Bottom Right' y 'Bottom Left'; el texto predicho y la puntuación de confianza de la predicción
results = reader.readtext(img, detail=1, paragraph=False)

# Para mostrar el texto en la imagen original o mostrar los 'bounding boxes' se necesitan las coordenadas del texto. Por lo
# que es necesario que el parámetro 'detail' de 'readtext' esté a '1'. Para cada 'bounding boxes', texto y puntuación de 
# cada texto capturado en la imagen...
for (bbox, text, prob) in results:

    # De las coordenadas de las 'bounding boxes' se extraen las coordenadas X e Y de los puntos 'Top Left', 'Top Right',
    # 'Bottom Right' y 'Bottom Left'
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    # Se elimina los caracteres no-ASCII para mostrar el texto limpio en la imagen
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

    # Se dibuja el rectángulo en la imagen especificando los puntos 'Top Left' y 'Bottom Right' con el color BGR y el
    # grosor especificados
    cv2.rectangle(img, tl, br, (0, 255, 0), 2)

    # Se escribe el texto en la imagen, un poco más arriba respecto al rectángulo de la 'bounding box' (se resta en
    # 10 puntos el Eje Y de la esquina 'Top Left')
    cv2.putText(img, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Para ver la imagen de salida
#cv2.imshow("Image", img)
#cv2.waitKey(0)

# Guarda la imagen de salida en el mismo directorio que la imagen de entrada pero con sufijo 'out'
cv2.imwrite('{}_out.jpg'.format(img_path[:-4]), img)