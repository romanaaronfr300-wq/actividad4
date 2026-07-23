#Secuencia de cuadros
N = int(input("Numero positivo: "))
i = 1

while True:
    print(i**2)
    i += 1
    if i > N:
        break
    
print("Secuencia de cuadros hasta", N)
