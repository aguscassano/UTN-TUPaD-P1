#------ FUNCIONES ------

#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print ("Hola Mundo!")


#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devovler  “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#4.Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio)
#que reciba el radio como parámetro y devuelva el perímetro del círculo.
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math #para usar el valor exacto de PI

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas (a, b):
    suma = a + b 
    resta = a - b
    multiplicacion = a * b
    division = a / b

    print(f"El resultado de la suma de {a} y {b} es: {suma}")
    print(f"El resultado de la resta de {a} y {b} es: {resta}")
    print(f"El resultado de la multiplicacion de {a} y {b} es: {multiplicacion}")
    print(f"El resultado de la división de {a} y {b} es: {division}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc (peso, altura):
    imc = peso / (altura ** 2)
    return imc


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#fahr = (9/5) * cel + 32

def celsius_a_fahrenheit(celsius):
    fahr = (9/5) * celsius + 32
    return fahr


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio





#------ PROGRAMA PRINCIPAL ------
#1 Llamar a esta función desde el programa principal.
imprimir_hola_mundo()

#2 Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.
print("--- Saludo a usuario ---")
usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(usuario)

#3 Pedir los datos al usuario y llamar a esta función con los valores ingresados
print("--- Datos de usuario ---")
name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
location = input("Ingresa la localidad donde vives: ")

info_personal = informacion_personal(name, last_name, age, location)

#4 Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
print("--- Area y perimetro de un circulo ---")
radio_circulo = int(input("Ingrese el radio de un circulo: "))
area_circulo = calcular_area_circulo(radio_circulo)

perimetro_circulo = calcular_perimetro_circulo(radio_circulo)

print(f"El area del circulo es {area_circulo}")
print(f"El perimetro del circulo es {perimetro_circulo}")

#5 Solicitar al usuario los segundos y mostrar el resultado usando esta función.
print("--- Segundos a horas ---")
seg = int(input("Ingrese una cantidad de segundos: "))

hora = segundos_a_horas(seg)
print(f"{seg} segundos equivalen a {hora} horas")

#6 Pedir al usuario el número y llamar a la función.
print("--- Tablas de multiplicación ---")
num = int(input("Ingrese un número del 1 al 10: "))

if num >= 1 and num <= 10:
    tabla_multiplicar(num)
else:
    print("El número ingresado no es correcto!")

#7 Mostrar los resultados de forma clara.
print("--- Operaciones básicas ---")
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro numero: "))

operaciones_basicas(num1, num2)

#8 Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
print("--- Calculo de IMC ---")
peso_usario = float(input("Ingrese su peso: "))
altura_usuario = float(input("Ingrese su altura (en metros): "))
masa_corporal = calcular_imc(peso_usario, altura_usuario)
print(f"Su IMC es de {masa_corporal:.2f}")

#9 Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
print("--- Celsius a Fahrenheit ---")
grados = float(input("Ingrese una temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(grados)

print(f"La temperatura {grados} °C es equivalente a {fahrenheit} grados Fahrenheit")

#10 solicitar los números al usuario y mostrar el resultado usando esta función.
print("--- Calculo de promedio (3 numeros) ---")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

prom = calcular_promedio(numero1, numero2, numero3)

print(f"El promedio de {numero1}, {numero2} y {numero3} es: {prom:.2f}")