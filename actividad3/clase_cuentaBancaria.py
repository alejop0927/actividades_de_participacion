class Cuenta_Bancaria:
    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta=numero_cuenta
        self.propietarios=propietarios
        self.balance=balance

    def depositar(self,cantidad_depositar):
        self.balance += cantidad_depositar
        self.dinero_actualizado= cantidad_depositar
        
    
    def retirar_dinero(self,cantidad_retiro):
        if cantidad_retiro <= self.balance:
          self.balance -= cantidad_retiro
          self.retirada=cantidad_retiro
        else:
            print(f"Fondos insuficientes para el retiro")

    def cuotaManejo(self):
        porcentaje=0.02 * self.balance
        self.balance -= porcentaje
        self.nuevo_saldo= porcentaje
    
    def mostrar_detalles(self):
        print(f"numero cuenta: {self.numero_cuenta}")
        print(f"propietario:{self.propietarios}")
        print(f"Balance actual:{self.balance}")
        print(f"el dinero depositado es: {self.dinero_actualizado}")
        print(f"la cantidad retirada de la cuenta es:{self.retirada}")
        print(f"la cuota de manejo es:{self.nuevo_saldo}")


        
cuenta1=Cuenta_Bancaria(123,"Juan",2000000)
cuenta1.depositar(0)
cuenta1.retirar_dinero(100000)
cuenta1.cuotaManejo()
cuenta1.mostrar_detalles()


        