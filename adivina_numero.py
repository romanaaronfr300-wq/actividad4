#adivina numero
import random
secreto = random.randint(1, 100)
print("Adivina el numero entre 1 y 100")
while True:
    intento = int(input("Introduce tu intento: "))
    if intento < secreto:
        print ("Demasiado bajo, intenta de nuevo")
    elif intento > secreto:
        print ("Demasiado alto, intenta de nuevo")
    else:
        print ("Felicidades, adivinaste el numero secreto", secreto)
        break
    print ("juego terminado. El numero era", secreto)