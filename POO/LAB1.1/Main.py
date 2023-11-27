from Cliente import Cliente


if __name__ == "__main__":

    usuario1 = Cliente()
    while True:
        iniciarmenu = int(input("Principal Page — ULagosBank\nSeleccione una opción:\n   1. Ingresar como Cliente.\n   2. Ingresar como Ejecutivo.\n   3. Cerrar.\n"))
        if iniciarmenu == 1:
            comando = int(input("Has ingresado al menu de Clientes, seleciona una de estas opciones: \n1. Selecionar producto Bancario. \n2. Realizar Deposito \n 3.Retirar saldo.\n "))
            if comando == 1:
                print("Si")
            elif comando == 2:
                usuario1.deposito()
            elif comando == 3:
                usuario1.retiro(float(input("Dinero a retirar: ")))
        elif iniciarmenur == 2:
            opcion = int(input("Has ingresado al menu de Ejecutivos, selecione una opción: \n 1. Crear Cliente. \n 2. Crear Cuenta \n 3. Crear Cuenta Joven"))
            if opcion == 1:
                print()

        elif iniciarmenu == 3:
            print("Se cerró el programa.")
            break
        else:
            print("Ingrese una opción Valida.")