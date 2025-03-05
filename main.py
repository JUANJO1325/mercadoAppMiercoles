#Aplicacion que nos permita ir a Mercar 


#Programa para gestion de productos
#En una lista de Mercado
nombreUsuario=None

#Declarando las Variables
productos=[]
producto={}

#Crear un menu de opciones
print("**MerqueoAPP***")
print("1. Aregar producto a tu lista de mercado")
print("2. Mostrar tu lista de mercado")
print("2. Modificar tu lista de mercado")
print("2. Retirar tu lista de mercado")

print(" Presiona 5 para SALIR")

opcion=100
while opcion != 5:
    opcion=int(input("Digita una opcion en el menu: "))

    if opcion == 1:
        print("Creando la lista")
        #Poblando listas y diccionarios en python 

        #Asignando claves a un diccionario
        producto["id"] = 5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["presentacion"]=input("Digite la presentación del producto: ")
        producto["cantidad"]=int(input("Digite la cantidad que desea del producto: "))
        producto["precio"]=int(input("Digite el precio del producto: "))

        print(producto)

    elif opcion == 2:
        print("Mostrando la lista")
    elif opcion == 3:
        print("Modificando la lista")
    elif opcion == 4:
        print("Retirando la lista")
    elif opcion == 5:
        print("Saliendo...")
    else:
        print("Opcion invalida")
