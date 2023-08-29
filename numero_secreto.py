
while True:
    
    numero_secreto = 3
    
    numero = input("digite un numero entero aleatorio: ")
    
    try:
        numero = int(numero)
    except:
        print("el numero es invalido, dijite un numero entero")
        
        continue
    if numero != numero_secreto:
        if numero > numero_secreto:
           print("el numero digitado es mayor al numero secreto")
         
        elif numero < numero_secreto:
           print("el numero  digitado es menor al numero secreto")
         
    else:
        print("FELICIDADES HAS ADIVINADO EL NUMERO SECRETO")
    break
        