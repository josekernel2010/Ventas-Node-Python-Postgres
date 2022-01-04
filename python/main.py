import os
import requests
from tabulate import tabulate


def iniciar():
    os.system("cls")
    while True:
        print("Escoja una de las siguientes opciones:")
        print("1. Registrar un producto")
        print("2. Consultar todos los productos")
        print("3. Buscar un producto")
        print("4. Modifiicar un producto")
        print("5. Eliminar un producto")
        print("6. Salir")
        opcion = input("Ingrese una opcion: ")
        os.system("cls")
        if opcion == "1":
            # registrar()
            pass
        elif opcion == "2":
            # consultar()
            pass
        elif opcion == "3":
            # buscar()
            pass
        elif opcion == "4":
            # modifiicar()
            pass
        elif opcion == "5":
            # eliminar()
            pass
        elif opcion == "6":
            break
        else:
            print("===============")
            print("Opcion invalida")
            print("===============")
            input("Presione una tecla para continuar...")
            os.system("cls")


iniciar()
