import cv2

cap = cv2.VideoCapture("road.mp4") #carga video

while True:
    ret, frame = cap.read()#leemos el video
    frame =cv2.resize(frame,(1280,720)) # redimension de video

    cv2.imshow("Autopista",frame) #reproducir video
    
    # el escape de la ventana de video
    key =cv2.waitKey(5)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



