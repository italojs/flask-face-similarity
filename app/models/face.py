import cv2
import base64
import numpy as np
import face_recognition

class Face():
    def __init__(self, b64):
        nparr = np.fromstring(base64.b64decode(b64), np.uint8)
        self.__img = cv2.imdecode(nparr,1)
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2RGB)


    def __face_bbox(self):
        return face_recognition.face_locations(self.__img,
		    model="hog")
    
    def __generate_encondings(self, boxes):
        # compute the facial embedding for the face
         self.__encoding = face_recognition.face_encodings(self.__img, boxes)
         return self.__encoding
    
    def generate_encondings(self):
        bboxes = self.__face_bbox()
        return np.asarray(self.__generate_encondings(bboxes), dtype=np.float64)

    def compare_self_with(self, encoding):
        return face_recognition.face_distance(
            self.__encoding, 
            encoding)