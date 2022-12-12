from time import sleep

cadena = '-' * 50
caracter = '#'
b = -1

print()

for i in range(100):
    if(i % 2 == 0) :
        b = b+1
        x = list(cadena)
        x[b] = caracter
        cadena = "".join(x)
    
    print(f'[{cadena}]{i+1}%', end='\r')
    sleep(0.01)

print()