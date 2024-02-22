import cv2
from rastreador import * #importamos el programa rasteador full

cap = cv2.VideoCapture("road.mp4") #carga video
seguimiento = rastreador() #obejto de segumiento 

deteccion = cv2.createBackgroundSubtractorMOG2(history=100000000, varThreshold= 13) # extrae los obejetos en movimiento

while True:
    ret, frame = cap.read()#leemos el video
    frame =cv2.resize(frame,(1280,720)) # redimension de video
    
    #Elegimos una zona de ineteres (y,x)
    zona = frame[10: 500, 320:650]

    #Creamos una mascara que vuelve el fondo negro y los objetos en moviento blancos
    mascara = deteccion.apply(zona)
    _, mascara = cv2.threshold(mascara, 254.8, 255, cv2.THRESH_BINARY) # se eliminan las tonalidades grises y se deja el blanco
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detecciones=[] #lista donde se almacena la información
 
    # dibujamos los contornos
    for cont in contornos:
        area = cv2.contourArea(cont)
        
        if  800 < area and area > 700: # si el area es mayor a 100 pixeles
            x, y, ancho, alto = cv2.boundingRect(cont)
            cv2.rectangle(zona,(x,y),(x + ancho, y + alto),(255,255,0),3) # dibujamos el rectangulo
            detecciones.append([x, y, ancho, alto]) # almacenamos la informacion de las detecciones
    
    #seguimineto de obejetos
    info_id = seguimiento.rastreo(detecciones)
    '''
    for inf in info_id:
        x, y, ancho, alto, id = inf
        cv2.putText(zona, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255),2)
        cv2.rectangle(zona,(x,y),(x + ancho, y + alto),(255,255,0),3)
    
    '''    
    print("id", info_id)
    
    cv2.imshow("Autopista",frame) #reproducir video
    cv2.imshow("Zona de interes",zona) #reproducimos video recortado a la zona de interes
    cv2.imshow("mascara",mascara)
    # el escape de la ventana de video
    key =cv2.waitKey(5)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



