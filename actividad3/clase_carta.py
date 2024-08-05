carta_picas="picas"
carta_corazon="corazon"
carta_diamante="diamante"
carta_trebol="trebol"

class Carta:
    def __init__(self,valor,pinta):
        self.valor=valor
        self.pinta=pinta
        print(f"el valor de la carta es:{self.valor}, la pinta es {self.pinta}")

carta=Carta("4",carta_picas)
