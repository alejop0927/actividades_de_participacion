import math

class Circulo:
    def __init__(self, centro,radio):
       self.centro=centro
       self.radio=radio

    def calcularArea(self):
        
        area=math.pi*(self.radio)**2
        print("el area es:",area)

    def calcularPerimetro(self):
        perimetro=2*math.pi*self.radio
        print("el perimetro es:", perimetro)

    def punto(self,x,y,h,k):
        self.x=x
        self.y=y
        self.h=h
        self.k=k
    def calcularDistancia(self):
        distancia=(self.x-self.h)**2 + (self.y-self.k)**2
        raiz=math.sqrt(distancia)
        if raiz <= self.radio:
            print("estan dentro del circulo")
        else:
            print("estan fuera de el circulo")

circulo=Circulo(12,12)
circulo.calcularArea()
circulo.calcularPerimetro()
circulo.punto(10,10,12,12)
circulo.calcularDistancia()






