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
            nuevo_producto()
            pass
        elif opcion == "2":
            consultar()
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


def nuevo_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    precio = input("Ingrese el precio del producto: ")
    # lista donde asignamos los valore obtenidos desde los input
    datos = {"nombre": nombre, "descripcion": descripcion, "precio": precio}
    # request post ingresa los datos dede python hasta la base de datos por medio de la ruta
    respuesta = requests.post(
        url="http://localhost:3000/producto/registro", data=datos)
    print(respuesta.text)


def consultar():

    respuesta = requests.get(url='http://localhost:3000/producto/todos')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'NOMBRE', 'DESCRIPCIÓN', 'PRECIO']
    pass


if __name__ == "__main__":

    iniciar()
