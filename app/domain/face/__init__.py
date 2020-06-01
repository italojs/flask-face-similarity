# import imghdr
import gc
import cv2
from app.models.face import Face

class FaceDomain:  

  def __init__(self, face1, face2):
      __slots__ = ('__face1', '__face2')
      self.__face1 = face1
      self.__face2 = face2

  def handdle(self):     
      face1 = Face(self.__face1)
      face1.generate_encondings()

      face2 = Face(self.__face2)
      encod = face2.generate_encondings()
      return face1.compare_self_with(encod)
  
