## Realice un programa que al ingresar un número, diga sus características, así como si es un primo,
## compuesto, par, impar, positivo y negativo.
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
        cursor.execute("SELECT * from codigo2;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["Intento", "Numero"], tablefmt="psql", numalign ="center"))
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
        Instruction = "insert into codigo2(numero) values('"+str(Numero)+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado su numero.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Jugar():

    validez = True

    while validez:
        print("Ingrese un numero entero entre 0 y 999")
        Entrada = input("Su elección: ")
        try:
            Numero = int(Entrada)
            if Numero<999 and Numero>0 and isinstance(Numero, int):
                validez=False
                break
            else:
                print("Ingrese una opción válida.\n")
        except:
            print("Ingrese una opción válida.\n")


    return Numero



opcion = " "

print("Bienvenidos al programa 'Números'")

while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Jugar \n'B' Ver historial \n'Z' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='A':
        numero = Jugar()
        if numero%2 ==0:
            print("El numero es par")
        else:
            print("El numero es impar")
        Post(numero)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")