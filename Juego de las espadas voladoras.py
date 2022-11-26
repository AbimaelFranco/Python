##En este juego se tiene un recipiente con 5 espadas, y los jugadores deberán adivinar
## cuantas espadas encajaran en los 5 espacios disponibles, el primer jugador que acierte 5 veces el número
## de espadas que encajan gana.
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
        cursor.execute("SELECT * from codigo4;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["No. de Juego", "Ganador"], tablefmt="psql", numalign ="center"))
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
        Instruction = "insert into codigo4(ganador) values('"+Ganador+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado su juego.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Jugar():

    validez = True
    Espadas = 5
    Restantes = Espadas
    Aciertos=0

    while validez:
        if(Restantes>0):
            Posicion = random.randint(1,Restantes)
        else:
            break
        # print("\nLa casilla de la espada es ", str(Posicion),"+++++++++++")
        while Restantes>0:
            print("Ingrese un entre 1 y ", Restantes)
            Entrada = input("Su elección: ")
            try:
                Numero = int(Entrada)

                if Numero<=Restantes and Numero>=1 and isinstance(Numero, int):
                    if(Posicion==Numero):
                        Aciertos = Aciertos+1
                        print("Ha acertado, lleva", str(Aciertos), " acertadas")
                        Restantes=Restantes-1
                        break
                    else:
                        print("Ha fallado")
                else:
                    print("Ingrese una opción válida.\n")
            except:
                print("Ingrese una opción válida.\n")

            if Restantes<=0:
                validez = False
                break
            else:
                PC = random.randint(1,Restantes)
                print("\nLa IA elije la posición: ", PC)
                if(Posicion==PC):
                    print("La IA a acertado")
                    Restantes=Restantes-1
                    break
                else:
                    print("Ha fallado\n")
                    # break
            
    if(Aciertos>=3):
        Ganador = "Gano"
        print("\nUsted gano")
    else:
        Ganador = "Perdio"
        print("\nUsted Perdio")

    return Ganador



opcion = " "

print("Bienvenidos al programa 'Espadas Voladoras'")

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