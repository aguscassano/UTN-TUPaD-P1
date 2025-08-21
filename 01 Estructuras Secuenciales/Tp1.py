#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.

name = input("Ingrese su nombre:")
print(f"Hola {name}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla

name = input("Ingrese su nombre:")
lastName = input("Ingrese su apellido:")
age = int(input("Ingrese su edad:"))
ubi = input("Ingrese su lugar de residencia:")

print(f"Soy {name} {lastName}, tengo {age} años y vivo en {ubi}")

#4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

rad = float(input("Ingrese el radio de un circulo:"))

pi = 3.14159
area = pi * (rad**2)
per = 2 * pi * rad

print (f"El area del criculo es {area}, el perimetro del circulo es {per}")

#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seg = int(input("Ingrese la cantidad de segundos:"))
hora = 1 / 3600
horEq = hora * seg

print ("La cantidad de segundos ingresada equivalen a", horEq, "horas")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un numero:"))

uno = num * 1
dos = num * 2
tres = num * 3
cuatro = num * 4
cinco = num * 5
seis = num * 6
siete = num * 7
ocho = num * 8
nueve = num * 9 
diez = num * 10

print (f"1 x {num} = {uno} - 2 x {num} = {dos} - 3 x {num} = {tres} - 4 x {num} = {cuatro} - 5 x {num} = {cinco} - 6 x {num} = {seis} - 7 x {num} = {siete} - 8 x {num} = {ocho} - 9 x {num} = {nueve} - 10 x {num} = {diez}")

#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero entero distinto de cero:"))
num2 = int(input("Ingrese otro numero entero distinto de cero:"))

suma = num1 + num2 
divi = num1 / num2
mult = num1 * num2
rest = num1 - num2

print (f"{num1} + {num2} = {suma} | {num1} / {num2} = {divi} | {num1} * {num2} = {mult} | {num1} - {num2} = {rest}")

#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente

altura = float(input("Ingrese su altura:"))
peso = float(input("Ingrese su peso:"))

imc = peso / (altura ** 2)

print (f"Su indice de masa corporal es de {imc}")

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

cel = float(input("Ingrese la temperatura en grados Celsius:"))
fahr = (9/5) * cel + 32

print (f"La temperatura ingresada en grados Celsius es equivalente a {fahr} grados Fahrenheit")

#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

nu1 = float(input("Ingrese un numero:"))
nu2 = float(input("Ingrese el segundo numero:"))
nu3 = float(input("Ingrese el tercer numero:"))

prom = (nu1 + nu2 + nu3) / 3

print ("El promedio de los numeros ingresados es de", prom)
