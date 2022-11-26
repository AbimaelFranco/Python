##Se tienen 3 dados, uno blanco, uno rojo y uno negro, cada uno tiene solo 3
## posibilidades, para el blanco es 1,5,9; para el negro es 3, 4, 8; y para el rojo es 6, 2 y 7; el usuario eleigrá un
## dado y la maquina uno de los dos que sobra, se giraran los dados y el que tenga el valor más alto gana.
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
        cursor.execute("SELECT * from codigo1;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["Juego", "Ganador"], tablefmt="psql", numalign ="center"))
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
        Instruction = "insert into codigo1(ganador) values('"+Ganador+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado la partida.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Jugar():
    Dado1 = random.randint(1,3)
    Dado2 = random.randint(1,3)
    PC = random.randint(1,3)
    PCE = " "
    # Elecion1 = 0
    # Elecion2 = 0

    Jugador = " "

    while True:
        print("Seleccione un dado del siguiente menú: \n'B' Blanco \n'N' Negro \n'R' Rojo")
        Jugador = input("Su elección: ").upper()

        if(Jugador=='B'):
            break
        elif(Jugador=='N'):
            break
        elif(Jugador=='R'):
            break
        else:
            print("Ingrese una opción válida.\n")

    if Jugador == 'B':
        if(Dado1==1):
            Elecion1 = 1
        elif(Dado1==2):
            Elecion1 = 5
        elif(Dado1==3):
            Elecion1 = 9
    elif Jugador == 'N':
        if(Dado1==1):
            Elecion1 = 3
        elif(Dado1==2):
            Elecion1 = 4
        elif(Dado1==3):
            Elecion1 = 8
    elif Jugador == 'R':
        if(Dado1==1):
            Elecion1 = 6
        elif(Dado1==2):
            Elecion1 = 2
        elif(Dado1==3):
            Elecion1 = 7

    iguales = True

    while iguales:
        if PC ==1:
            PCE = "B"
        elif PC==2:
            PCE = "N"
        elif PC==3:
            PCE = "R"
        
        condicion = PCE is Jugador

        if not condicion:
            iguales= False


    if PCE == 'B':
        if(Dado2==1):
            Elecion2 = 1
        elif(Dado2==2):
            Elecion2 = 5
        elif(Dado2==3):
            Elecion2 = 9
    elif PCE == 'N':
        if(Dado2==1):
            Elecion2 = 3
        elif(Dado2==2):
            Elecion2 = 4
        elif(Dado2==3):
            Elecion2 = 8
    elif PCE == 'B':
        if(Dado2==1):
            Elecion2 = 6
        elif(Dado2==2):
            Elecion2 = 2
        elif(Dado2==3):
            Elecion2 = 7

    if(Elecion1>Elecion2):
        Ganador = "Gano"
    else:
        Ganador = "Perdio"

    print("Usted", Ganador)
    return Ganador

opcion = " "

print("Bienvenidos al programa 'Juego del Club Literario'")

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