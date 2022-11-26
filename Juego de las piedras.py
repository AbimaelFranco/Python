##Este es un juego que consiste en que se tienen 181 piedras en un recipiente, y el que retire la última
## pierde, para definir cuantas saca se tirara un dado común y corriente y se extraerá el número que este dicte,
## en este caso será un juego contra "la máquina" y solo serán 91 piedras, el jugador podrá ir apostando en
## cada turno según vea si gana o no, se deberá decir si ganó la máquina o el usuario y guardarlo en la base de datos.
##NOTA: Se deberan modificar los campos de la función 'Historial' según la base de datos empleada.

import random
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
        cursor.execute("SELECT * from codigo3;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["No. de Juego", "ganador"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")

def Post(Ganador):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5433",
            user = "postgres",
            password = "pass",
            dbname = "examen1"
            )
        cursor = conexion.cursor()
        Instruction = "insert into codigo3(ganador) values('"+Ganador+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado su juego.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Jugar():

    validez = True
    piedras = 91
    total = piedras
    while validez:
        print("Hay ", total, "en el recipiente.")
        Entrada = input("Precione enter para continuar")
        quitar = random.randint(1,6)
        print("Usted intenta quitar", str(quitar))
        total = total-quitar
        
        if total<=0:
            print("Ya no hay piedras, usted perdio")
            Ganador = "Perdio"
            validez = False
            break

        quitar = random.randint(1,6)
        print("El computador intenta quitar", str(quitar))
        total = total-quitar
        if total<=0:
            print("Ya no hay piedras, usted gano")
            Ganador = "Gano"
            validez = False
            break

    return Ganador



opcion = " "

print("Bienvenidos al programa 'Nim con dados'")

while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Jugar \n'B' Ver historial \n'Z' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='A':
        ganador = Jugar()
        Post(ganador)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")