'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.

YUSMEL BARRIOS TRUJILLO
INGENERIA EN SISTEMAS.

'''
class CuentaBancaria:
    def __init__(self, numero_cta, nombre_cliente, saldo_cta, fecha_apertura):
        self.numero_cta = numero_cta
        self.nombre_cliente = nombre_cliente
        self.saldo_cta = saldo_cta
        self.fecha_apertura = fecha_apertura
        self.ultimo_retiro = 0
        self.ultima_consignacion = 0

    def consignar(self, monto):
        self.saldo_cta += monto
        self.ultima_consignacion = monto
        print("Consignación realizada correctamente.")

    def retirar(self, monto):
        if monto <= self.saldo_cta:
            self.saldo_cta -= monto
            self.ultimo_retiro = monto
            print("Retiro realizado correctamente.")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_datos_cuenta(self):
        print(f"Número de cuenta: {self.numero_cta}")
        print(f"Titular: {self.nombre_cliente}")
        print(f"Saldo actual: {self.saldo_cta}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Último retiro: {self.ultimo_retiro}")
        print(f"Última consignación: {self.ultima_consignacion}")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear nueva cuenta bancaria")
        print("2. Salir")
        opcion_principal = int(input("Ingrese la opción deseada: "))

        if opcion_principal == 1:
            numero_cta = int(input("Ingrese el número de cuenta: "))
            nombre_cliente = input("Ingrese el nombre del titular: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            fecha_apertura = input("Ingrese la fecha de apertura: ")

            mi_cuenta = CuentaBancaria(numero_cta, nombre_cliente, saldo_inicial, fecha_apertura)

            while True:
                print("\n--- Menú de opciones ---")
                print("1. Consultar saldo")
                print("2. Realizar consignación")
                print("3. Realizar retiro")
                print("4. Mostrar datos de la cuenta")
                print("5. Volver al menú principal")
                opcion = int(input("Ingrese la opción deseada: "))

                if opcion == 1:
                    print(f"Saldo actual: {mi_cuenta.saldo_cta}")
                elif opcion == 2:
                    monto_consignacion = float(input("Ingrese el monto a consignar: "))
                    mi_cuenta.consignar(monto_consignacion)
                elif opcion == 3:
                    monto_retiro = float(input("Ingrese el monto a retirar: "))
                    mi_cuenta.retirar(monto_retiro)
                elif opcion == 4:
                    mi_cuenta.mostrar_datos_cuenta()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion_principal == 2:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
