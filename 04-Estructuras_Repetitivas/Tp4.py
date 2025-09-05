# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range (101):
    print (num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de  dígitos que contiene.

numero = int(input("Ingrese un numero entero:"))
cant_digitos = len(str(numero))
print ("La cantidad de digitos del numero ingresado es: ",cant_digitos)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range (num1 + 1,num2):
    suma += i

print ("La suma de los numeros entre", num1, "y", num2, "es", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

CORTE = 0
total = 0

num_entero = int(input("Ingresa un número entero (Ingrese 0 para finalizar): "))
while num_entero != CORTE:
    total += num_entero
    num_entero = int(input("Ingrese otro número (Ingrese 0 para finalizar):"))
print("La sumatoria de los números ingresados es",total)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_random = random.randint(0, 9)
cont = 1

numero_entero = int(input("Ingrese un número entero entre el 0 y el 9!:"))
while numero_entero != numero_random:
    numero_entero = int(input("No acertaste! Ingresa otro número: "))
    cont += 1
print ("Acertaste! El número era:", numero_random, "La cantidad de intentos fue", cont)


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range (100,0,-2):
    print(numero)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
res_suma = 0
num_ent = int(input("Ingrese un numero entero: "))

for x in range (0, num_ent + 1):
    res_suma += x
print("La suma de los número comprendidos entre 0 y", num_ent, "es", res_suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
positivo = 0
negativo = 0

for cien in range (0,5): #cambiar para ingresar 100 numeros
    num_cien = int(input("Ingrese un numero entero: "))
    if num_cien % 2 == 0:
        par += 1
    else:
        impar += 1
    if num_cien < 0:
        negativo += 1
    else:
        positivo += 1

print ("La cantidad de números pares ingresados son:", par, "La cantidad de números impares:" , impar, "La cantidad de números positivos:", positivo, "La cantidad de numeros negativos:", negativo)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

prom_cont = 0

for promedio in range (1,10):#cambiar para ingresar 100 numeros
    num_prom = int(input("Ingrese un número: "))
    prom_cont += num_prom

print("El promedio de los numeros ingresados es", (prom_cont/10))

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_inv = int(input("Ingrese un número: "))

invertido = 0

while num_inv > 0:
    digito = num_inv % 10
    invertido = invertido * 10 + digito
    num_inv = num_inv // 10

print ("El número invertido es: ", invertido)
