#Imprimir los primeros 10 numeros pares

n=int(input("Ingresa el numero desde donde empezar a buscar los pares"))
i=1
while i<=10:
    if n%2==0:
        print(n)
        i+=1
    n+=1