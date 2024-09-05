"""
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
"""


class Cuentabancaria:
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
        self.__numerocuenta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion

    def set_numerocuenta(self, x):
        self.__numerocuenta = x

    def set_nombre_cliente(self, x):
        self.__nombreCliente = x

    def set_saldo(self, x):
        self.__saldoCta = x

    def set_fecha_apertura(self, x):
        self.__fechaApertura = x

    def set_ultimo_retiro(self, x):
        self.__ultimoRetiro = x

    def set_ultima_consignacion(self, x):
        self.__ultimaConsignacion = x

    def get_numerocuenta(self):
        return self.__numerocuenta

    def get_nombre_cliente(self):
        return self.__nombreCliente

    def get_saldo(self):
        return self.__saldoCta

    def get_fecha_apertura(self):
        return self.__fechaApertura

    def get_ultimo_retiro(self):
        return self.__ultimoRetiro

    def get_ultima_consignacion(self):
        return self.__ultimaConsignacion

mi_cuenta = Cuentabancaria(
         numeroCta=input("ingrese su numero de cuenta: ")
    ,    nombreCliente="YUSMEL BARRIOS", saldoCta=1000000,
                           fechaApertura="2024-011-15", ultimoRetiro=50000, ultimaConsignacion=800000)

###print("Número de cuenta: ", mi_cuenta.get_numerocuenta())
print("Nombre del cliente: ", mi_cuenta.get_nombre_cliente())
print("Saldo actual:", mi_cuenta.get_saldo())
print("su fecha de apertura fue : ", mi_cuenta.get_fecha_apertura())
print("su ultimo retiro fue :", mi_cuenta.get_ultimo_retiro())
print("su ultima consignacion fue :", mi_cuenta.get_ultima_consignacion())
