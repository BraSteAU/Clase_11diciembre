#Imprimir los numeros impares desde el 1 hasta el numero ingresado

num=int(input("Ingrese numero entero positivo "))
n=1
while n<=num:
    if n%2!=0:
        print(n)
    n+=1