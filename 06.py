#Calcular el factorial de un numero ingresado

num = int(input("Ingrese un numero entero positivo: "))
factorial=1
i=1
while i<num:
    factorial+=factorial*i
    i+=1
print(f"El factorial de {num} es: {factorial}")
