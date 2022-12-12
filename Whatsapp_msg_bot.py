import pyautogui, webbrowser
from time import sleep

def main():

    print("Hola, que desea realizar:",
        "\n1) Enviar mensaje"
        "\n2) Ver contactos"
    )

    Opcion = input("Ingrese el número de opción: ")

    try:
        if int(Opcion) == 1:

            contact = input("\nIngrese el número teléfonico del contacto o el nombre con el que está registrado: ")
            message = input("\nIngrese su mensaje: ")
            times = int(input("\n¿Cúantas veces desea enviar el mensaje? (solo número): "))

            print("\n¿Está seguro de enviar el mensaje: \"", message, "\" a ", contact, " ", times, " veces ?")

            print()

            confirmation = " "

            while True:
                if (confirmation == "si" or confirmation == "no"):
                    break
                else:
                   confirmation = input("Ingrese \"si\" o \"no\" para confirmar: ")
                   print() 

            if confirmation == "si":
                send_message(contact, message, times)
                print()
            else:
                return

        elif int(Opcion) == 2:

            print("Contacts list")

        else:
            print("Opción no válida")

    except:
        print("Opción ingresada inválida")

def send_message(contact, message, times):

    contact = 'https://web.whatsapp.com/send?phone=+'+contact
    cadena = '-' * (50)
    caracter = '#'
    
    webbrowser.open(contact)

    sleep(10)

    print()

    for i in range(times):
        pyautogui.typewrite(message)   #Ingresa el mensaje en el navegador
        pyautogui.press('enter')  #Envia el mensaje

        # print(message)    #Este solo es para ver el mensaje

        b = round(((i) / times) * 50)
        x = list(cadena)
        x[b-1] = caracter
        cadena = "".join(x)
        
        #Formato de carga 1
        print("Mensajes enviados con éxito:", f'{i+1} de {times}', end='\r')

        #Formato de carga 2
        # print(f'[{cadena}]{(b)*2}%', end='\r')

    
    print()


main()