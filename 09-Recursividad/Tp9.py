#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

num_factorial = int(input("Ingrese un numero para calcular su factorial: "))

print(f"El factorial de {num_factorial} es {factorial(num_factorial)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibonacci (posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    

num_fibonacci = int(input("Ingrese un numero para calcular el valor de la serie de Fibonacci: "))

for i in range(num_fibonacci):
    print(fibonacci(i))


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recursiva (n,m):
    if n == 0 or m == 0:
        return 0 
    else:
        return n * n**(m-1)
    

num1 = int(input("Ingrese un numero base para calcular la potencia: "))
num2 = int(input("Ingrese el exponente para calcular la potencia: "))

print(f"La potencia de {num1} elevado a {num2} es {potencia_recursiva(num1,num2)}")


#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_binario (d):
    if d < 2:
        return str(d)
    else:
        cociente = d // 2
        resto = d % 2
        return decimal_binario(cociente) + str(resto)
    

decimal = int(input("Ingrese un numero decimal para convertirlo en binario: "))

print(f"El numero {decimal} en binario es {decimal_binario(decimal)}")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 

def es_palindromo(palabra):
    if len(palabra) < 2:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_palindromo = input("Ingrese una palabra: ").lower().strip()

print(f"La palabra {palabra_palindromo} es {es_palindromo(palabra_palindromo)}")


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto_num = n // 10
        return ultimo_digito + suma_digitos(resto_num)
    

sumar_digito = int(input("Ingrese un numero: "))
print(f"La suma de los digitos de {sumar_digito} es = {suma_digitos(sumar_digito)}")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
# Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    

base_piramide = int(input("Ingrese la cantidad de bloques que tiene la base de la piramide: "))

print(f"La piramide con base {base_piramide} necesita {contar_bloques(base_piramide)} para ser construida")


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10

    if ultimo_digito == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return contar_digito(resto_numero, digito)
    
numero = int(input("Ingrese un numero para contar los digitos: "))
digito = int(input("Ingrese un digito que desea contar (0 a 9): "))

print(f"La cantidad de veces que aparece {digito} en {numero} es {contar_digito(numero, digito)}")