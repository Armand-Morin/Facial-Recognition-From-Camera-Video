import cv2
import numpy as np
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0) #Si vous souhaitez utiliser une vidéo déjà enregistrée sur votre ordinateur, il suffit de remplacer le 0 par le chemin de votre fichier
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner1.yml')
Name='Unknown'
id=0
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if id == 2:
            Name='Armand'
        cv2.putText(img,Name,(x,y+h),font,3,(255,0,0),3)
    cv2.imshow('frame',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
