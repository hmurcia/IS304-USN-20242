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

    # Métodos para establecer y obtener atributos (encapsulamiento)

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de opciones ---")
            print("1. Consultar saldo")
            print("2. Realizar consignación")
            print("3. Realizar retiro")
            print("4. Transferencia")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                print("Saldo actual:", self.get_saldo())
            elif opcion == "2":
                monto = float(input("Ingrese el monto a consignar: "))
                self.set_ultima_consignacion(monto)
                self.set_saldo(self.get_saldo() + monto)
                print("Consignación realizada correctamente.")
            elif opcion == "3":
                monto = float(input("Ingrese el monto a retirar: "))
                if monto <= self.get_saldo():
                    self.set_ultimo_retiro(monto)
                    self.set_saldo(self.get_saldo() - monto)
                    print("Retiro realizado correctamente.")
                else:
                    print("Saldo insuficiente para realizar el retiro.")
            elif opcion == "4":
                # Implementa la lógica para transferencias
                pass
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    mi_cuenta = Cuentabancaria(
        numeroCta=input("Ingrese su número de cuenta: "),
        nombreCliente="YUSMEL BARRIOS",
        saldoCta=1000000,
        fechaApertura="2024-01-15",
        ultimoRetiro=50000,
        ultimaConsignacion=800000
    )
    mi_cuenta.mostrar_menu()
