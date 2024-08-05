class Punto:
   def __init__(self,coordenada_x, coordenada_y):
    self.coordenada_x=coordenada_x
    self.coordenada_y=coordenada_y

   def mostrarCoordenadas(self):
    print(f"las coordendas son: \n en x: {self.coordenada_x} en y: {self.coordenada_y}")

   def moverCoordenadas(self,nueva_coordenada_x=3,nueva_coordenada_y=1):
     self.nueva_coordenada_x=nueva_coordenada_x
     self.nueva_coordenada_y=nueva_coordenada_y
     print(f"las nuevas coordenadas son:\n en X: {self.nueva_coordenada_x} en y: {self.nueva_coordenada_y}")
    
   def calcularDistancia(self): 
     resta_1=self.coordenada_x-self.nueva_coordenada_x
     resta_2=self.coordenada_y-self.nueva_coordenada_y
     print("la distancia en x es:", resta_1, "la resta distancia en y es:", resta_2)

punto1=Punto(5,6)
punto1.mostrarCoordenadas()
punto1.moverCoordenadas()
punto1.calcularDistancia()
      
