import os
import requests
from tabulate import tabulate
import pyfiglet
# 0. menu


def iniciar():
    os.system("cls")

    try:
        while True:
            titulo = 'Sistema de Ventas'
            a = pyfiglet.figlet_format(titulo)
            print(a)
            print("===========================================")
            print(":: Escoja una de las siguientes opciones ::")
            print("===========================================")
            print("\n\t1. Registrar un producto")
            print("\t2. Consultar todos los productos")
            print("\t3. Buscar un producto")
            print("\t4. Modifiicar un producto")
            print("\t5. Eliminar un producto")
            print("\t6. Nueva venta")
            print("\t7. Salir")
            opcion = input("\nIngrese una opcion: ")
            os.system("cls")
            if opcion == "1":
                nuevo_producto()
                pass
            elif opcion == "2":
                ver_todos()
                pass
            elif opcion == "3":
                buscar()
                pass
            elif opcion == "4":
                modifiicar()
                pass
            elif opcion == "5":
                eliminar()
                pass
            elif opcion == "6":
                nueva_venta()
            elif opcion == "7":
                break
            else:
                print("===============")
                print("Opcion invalida")
                print("===============")
                input("Presione una tecla para continuar...")
                os.system("cls")
    except:

        print("\n***********************************")
        print(':: Error de conección ¯\_(ツ)_/¯ ::')
        print("***********************************")
        input("Presione una tecla para continuar...")
        iniciar()


def tabla_producto(respuesta):
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'NOMBRE', 'DESCRIPCIÓN', 'PRECIO']
    tabla = tabulate(datos, headers, tablefmt="fancy_grid")
    print(tabla)


# 1. Registrar un producto
def nuevo_producto():
    print("===============================")
    print(":: Ingreso de nuevo producto ::")
    print("===============================\n")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    precio = input("Ingrese el precio del producto: ")
    # lista donde asignamos los valore obtenidos desde los input
    datos = {"nombre": nombre, "descripcion": descripcion, "precio": precio}
    # request post ingresa los datos dede python hasta la base de datos por medio de la ruta
    respuesta = requests.post(
        url="http://localhost:3000/producto/registro", data=datos)

    print(len(respuesta.text)*"=")
    print(respuesta.text)
    print(len(respuesta.text)*"=")
    input("Presione una tecla para continuar...")
    os.system("cls")


# 2. Consultar todos los productos
def ver_todos():
    respuesta = requests.get(url='http://localhost:3000/producto/todos')
    tabla_producto(respuesta)
    input("Presione una tecla para continuar...")
    os.system("cls")


# 3. Buscar un producto
def buscar():
    print("===========================")
    print(":: Busqueda de producto ::")
    print("===========================\n")
    try:

        id = input("\tIngrese el id : ")
        if id == "":
            print("\n*********************************")
            print("No se ingreso ningún valor id !!!")
            print("*********************************")
            input("Presione una tecla para continuar...")
            os.system("cls")
            return False
        respuesta = requests.get(
            url='http://localhost:3000/producto/buscar/'+id)

        if len(respuesta.json()) > 0:
            tabla_producto(respuesta)
        else:
            print("\n---------------------------")
            print(":: El producto no existe ::")
            print("---------------------------")
        input("Presione una tecla para continuar...")
        os.system("cls")

    except:
        print("\n***********************")
        print("*  Valor invalido !!! *")
        print("***********************")
        input("Presione una tecla para continuar...")
        os.system("cls")


# 4. Modifiicar un producto
# arreglar y acomodar
#
def modifiicar():
    print("===============================")
    print(":: Modificación de producto ::")
    print("===============================\n")
    id = input("\tIngrese el id: ")

    try:

        buscar = requests.get(url='http://localhost:3000/producto/buscar/'+id)

        if len(buscar.json()) > 0:
            campo = '4'

            while True:
                os.system("cls")
                tabla = tabulate(buscar.json(), tablefmt="fancy_grid")
                print(tabla)
                campo = input(
                    "\n\t1. Nombre\n\t2. Descripcion\n\t3. Precio\n\t4. Salir\n\tIngrese una opcion: ")

                if campo == '4':
                    os.system("cls")
                    return False
                if int(campo) > 3 or int(campo) < 1:
                    print("\nValor fuera de rango")
                    input("Presione una tecla para continuar...")
                    os.system("cls")
                    return False

                nuevoValor = input("Ingrese el nuevo valor: ")
                data = {'campo': campo, 'nuevoValor': nuevoValor}
                respuesta = requests.post(
                    url="http://localhost:3000/producto/modificar/" + id, data=data)
                print(len(respuesta.text)*"=")
                print(respuesta.text)
                print(len(respuesta.text)*"=")
                input("Presione una tecla para continuar...")
                os.system("cls")
                return False
        else:
            print("\n---------------------------")
            print(":: El producto no existe ::")
            print("---------------------------")
            input("Presione una tecla para continuar...")
            os.system("cls")

    except:
        print("\n***********************")
        print("*  Valor invalido !!! *")
        print("***********************")
        input("Presione una tecla para continuar...")
        os.system("cls")
# 5. Eliminar un producto


def eliminar():
    print("=============================")
    print(":: Eliminación de producto ::")
    print("=============================\n")
    id = input("Ingrese el id del producto: ")

    try:
        buscar = requests.get(url='http://localhost:3000/producto/buscar/'+id)
        tabla = tabulate(buscar.json(), tablefmt="fancy_grid")
        print(tabla)

        if len(buscar.json()) > 0:
            respuesta = requests.post(
                url='http://localhost:3000/producto/eliminar/'+id)

            print("\n", len(respuesta.text)*"=")
            print(respuesta.text)
            print(len(respuesta.text)*"=")
            input("Presione una tecla para continuar...")
            os.system("cls")

        else:
            print("\n---------------------------")
            print(":: El producto no existe ::")
            print("---------------------------")
            input("Presione una tecla para continuar...")
            os.system("cls")
    except:
        print("\n***********************")
        print("*  Valor invalido !!! *")
        print("***********************")
        input("Presione una tecla para continuar...")
        os.system("cls")
# 6. Nueva venta


def nueva_venta():
    print("\n\t*********************")
    print("\t:::  Nueva venta  :::")
    print("\t*********************\n")
    cliente = input("\tNombre del cliente: ")
    total = 0
    productos = []

    try:
        while True:
            print("\n--------------------------------------------")
            print("Seleccione el id del producto o 0 para salir")
            print("--------------------------------------------")
            id = input("\nIngrese el id del producto: ")
            os.system("cls")
            if id == '0':
                os.system("cls")
                break
            else:
                # Producto es de tipo 'list'
                producto = requests.get(
                    url='http://localhost:3000/producto/buscar/'+id)

                # len(producto) > 0 significa que el producto existe
                # ya que ahora es de tipo int por 'len'
                if len(producto.json()) > 0:
                    nombre = producto.json()[0]['nombre']
                    precio = producto.json()[0]['precio']

                    tabla = tabulate(
                        producto.json(), tablefmt="fancy_grid")
                    print("\n\n")
                    print(tabla)
                    print("\n\n")
                    cantidad = input("\tIngrese la cantidad: ")
                    os.system("cls")
                    total_producto = int(cantidad) * float(precio)
                    total += total_producto
                    productos.append(
                        [id, nombre, precio, cantidad, total_producto])
                    mostrar_venta(cliente, productos, total)
                else:
                    # os.system("cls")
                    print("\n\t****************************")
                    print("\t:: El producto no existe ::")
                    print("\t****************************")
                    # input("Presione una tecla para continuar...")
                    # os.system("cls")

    except:
        print("\n***********************")
        print("*  Valor invalido !!! *")
        print("***********************")
        input("Presione una tecla para continuar...")
        os.system("cls")

# 7. Mostrar la venta


def mostrar_venta(cliente, productos, total):
    print("\n\t==============================")
    print("\t:::  Comprobante de venta  :::")
    print("\t==============================")
    print("\nCliente: ", cliente, "\n")
    headers = ['ID', 'NOMBRE', 'PRECIO', 'CANTIDAD', 'TOTAL']
    tabla = tabulate(productos, headers, tablefmt="simple")
    print(tabla)
    print("\n\t\t\tTotal a pagar: ", total)


if __name__ == "__main__":

    iniciar()
