#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número: "))

if num % 2:
    print("El numero ingresado es impar!")
else:
    print("El numero ingresado es par!")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#Niño/a: menor de 12 años - Adolescente: mayor o igual que 12 años y menor que 18 años. - Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#Adulto/a: mayor o igual que 30 años.

Edad = int(input("Ingrese su edad: "))

if Edad < 12 and Edad >= 0:
    print("Niño/a")
elif Edad >= 12 and Edad < 18:
    print ("Adolescente")
elif Edad >= 18 and Edad < 30:
    print("Adulo/a joven")
elif Edad >= 30:
    print("Adulto/a")
else:
    print("Ingrese un numero válido!")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

pw = input("Ingrese una contraseña: ")

if len (pw) >= 8 and len (pw) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda,su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")


if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("La distribución no cumple estrictamente con los criterios de sesgo definidos.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla

frase = input("Ingrese una frase o palabra: ")
ult_caracter = frase[-1]

if ult_caracter == "a" or ult_caracter == "A":
    print (frase, "!")
elif ult_caracter == "e" or ult_caracter == "E":
    print (frase, "!")
elif ult_caracter == "i" or ult_caracter == "I":
    print (frase, "!")
elif ult_caracter == "o" or ult_caracter == "O":
    print (frase, "!")
elif ult_caracter == "u" or ult_caracter == "U":
    print (frase, "!")
else:
    print (frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:

name = input("Ingrese su nombre: ")
mayu = int(input("Ingrese 1, 2, 3 dependiendo de la oopcion que desee: 1. Si quiere su nombre en mayúsculas. 2. Si quiere su nombre en minúsculas. 3. Si quiere su nombre con la primera letra mayúscula."))

nameUpper = name.upper()
nameLower = name.lower()
nameTitle = name.title()
if mayu == 1: 
    print (nameUpper)
elif mayu == 2:
    print(nameLower)
elif mayu == 3:
    print(nameTitle)
else:
    print ("El numero ingresado no es correcto")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado

mag = float(input("Ingrese la magnitud del terremoto: "))

if mag < 3:
    print("Muy leve")
elif mag >= 3 and mag < 4:
    print("Leve")
elif mag >=4 and mag < 5:
    print("Moderado")
elif mag >= 5 and mag < 6:
    print("Fuerte")
elif mag >= 6 and mag < 7:
    print ("Muy fuerte")
elif mag >= 7:
    print ("Extremo")
else:
    print ("El numero ingresado no es correcto")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemi = input("Ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese que dia es (numero): "))

# Validaciones básicas mínimas (solo rango general)
if not (hemi in ("N", "n", "S", "s")):
    print("Hemisferio inválido (use N o S).")
elif not (1 <= mes <= 12):
    print("Mes inválido (1-12).")
elif not (1 <= dia <= 31):
    print("Día inválido (1-31).")
else:
    # 21/12–20/03
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        if hemi == "N" or hemi == "n":
            print("Invierno")
        else:  # S o s
            print("Verano")

    # 21/03–20/06
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        if hemi == "N" or hemi == "n":
            print("Primavera")
        else:
            print("Otoño")

    # 21/06–20/09
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        if hemi == "N" or hemi == "n":
            print("Verano")
        else:
            print("Invierno")

    # 21/09–20/12
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        if hemi == "N" or hemi == "n":
            print("Otoño")
        else:
            print("Primavera")

    else:
        # Si cae acá, probablemente el día no existe para ese mes (p.ej. 31/04),
        # pero como no usamos listas/validaciones avanzadas, avisamos genéricamente:
        print("Fecha fuera de los rangos considerados.")