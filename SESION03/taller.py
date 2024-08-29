'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
"""
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
"""


class Cuentabancaria:
    def __init__(self,numeroCta, nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
        set(numeroCta, nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion)

    def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
        self.__numerocuenta = numerocuenta
        self.__nombreCliente =  nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura= fechaApertura
        self.__ultimoRetiro= ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion

    def set_num(self,x):
        self.numerocuenta= x

    def set_num(self,x):
        self.nombreCliente= x
        
    def set_num(self,x):
        self.saldoCta= x
        
    def set_num(self,x):
        self.fechaApertura= x
    
    def set_num(self,x):
        self.numerocuenta= x
    
    def set_num(self,x):
        self.ultimoRetiro= x
        
    def set_num(self,x):
        self.ultimaConsignacion= x
        

    def set_den(self, x):
        if x == 0:
            self.den = 1
        else:
            self.den = x

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

def main():
    b = 23
    fr = Fraccion()
    fs = Fraccion(3, 5)
    #fr.set_num(1)
    fr.set_den(0)
    fr.den = 0
    print(f"{fr.get_num()}/{fr.get_den()}")
    print(f"{fs.get_num()}/{fs.get_den()}")
    fs.set(8, 9)
    print(f"{fs.get_num()}/{fs.get_den()}")

if __name__ == "__main__":
    main()
'''
