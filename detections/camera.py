import cv2
import cv2.data

class Camera():
    model = "haarcascade_frontalface_default.xml"
    
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + self.model)
    
    def __del__(self) -> None:
        self.video.release()
        
    def get_frame(self) -> bytes:
        s, img = self.video.read()
        img = cv2.flip(img, 1)
        faces = self.face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1 , 4)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
        
        _, jpeg = cv2.imencode(".jpg", img)
        return jpeg.tobytes()