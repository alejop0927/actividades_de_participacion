class Rectangulo:
    def __init__(self, esquina_superiorD,esquina_inferiorI):
        self.esquina_superiorD=esquina_superiorD
        self.esquina_inferiorI=esquina_inferiorI

    def Perimetro(self,esquina_superiorI=10):
        self.esquina_superiorI=esquina_superiorI
        self.longitud_H=self.esquina_superiorD-esquina_superiorI
        self.longitud_V=self.esquina_superiorI-self.esquina_inferiorI
        peri=2*(self.longitud_H + self.longitud_V)
        print("el perimetro es:", peri)
    
    def calcularArea(self):
        area=self.longitud_H*self.longitud_V
        print("el area es:",area)
        if self.longitud_H == self.longitud_V:
            print("es cuadrado")
        else:
            print("es rectangulo")



rectangulo=Rectangulo(13,6)
rectangulo.Perimetro()
rectangulo.calcularArea()


