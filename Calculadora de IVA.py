##Que ingrese un precio en quetzales, e indique cuanto de esa totalidad es IVA y cuanto es el precio sin IVA.
##Considerar que el IVA en Guatemala es el 12% del precio del producto.
##NOTA: Se deberan modificar los campos de la función 'Historial' según la base de datos empleada.

import psycopg2
from tabulate import tabulate

##Los siguientes parámetros deberan ser modificados según la base de datos que se emplee.
def Historial():
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5433",
            user = "postgres",
            password = "pass",
            dbname = "examen1"
            )
        cursor = conexion.cursor()
        cursor.execute("SELECT * from codigo5;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["No. Producto", "Precio"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")

def Post(Numero):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5433",
            user = "postgres",
            password = "pass",
            dbname = "examen1"
            )
        cursor = conexion.cursor()
        Instruction = "insert into codigo5(precio) values('"+str(Numero)+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado el precio de su producto.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Jugar():

    validez = True

    while validez:
        print("Ingrese el precio del producto")
        Entrada = input("Q")
        try:
            Numero = int(Entrada)
            Precio_total=Numero
            IVA=Numero*0.12
            Precio_sin_IVA = Precio_total-IVA

            print("El precio del producto sin iva es de: Q", str(Precio_sin_IVA)," por lo que su IVA es de: Q", str(IVA))

            validez=False
            break

        except:
            print("Ingrese una numero válida.\n")


    return Numero



opcion = " "

print("Bienvenidos al programa 'Calculadora de IVA'")

while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Jugar \n'B' Ver historial \n'Z' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='A':
        numero = Jugar()
        Post(numero)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")