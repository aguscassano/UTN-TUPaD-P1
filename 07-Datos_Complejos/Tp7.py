#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

lista_frutas = []
for i in precios_frutas:
    lista_frutas.append(i)
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}
print(contactos)

for x in range(0, 2):
    contacto = input("Ingrese un contacto: ")
    contactos[contacto] = 0
    numero = int(input("Ingrese el numero del contacto: "))
    contactos[contacto] = numero
print("Contactos guardados correctamente!")
nombre = input("Ingrese un nombre de contacto para consultar: ")
if nombre in contactos:
    print(f"El numero de {nombre} es: {contactos[nombre]}")
else:
    print("No existe un contacto asociado al nombre ingresado.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()
unicas = set(palabras)
print(unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print("Conteo: ", conteo)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

for a in range (0, 3):
    alumno = input("Ingrese el nombre del alumno: ")
    alumnos[alumno] = []
    notas = []
    
    for n in range (0, 3):
        notas.append(int(input("Ingrese una nota: ")))
    alumnos[alumno] = tuple(notas)


for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 4, 7, 8, 9}
parcial2 = {2, 7, 3, 9, 11, 1}

ambos = parcial1 & parcial2
print(f"Aprobaron ambos parciales: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Aprobraron solo uno de los parciales: {solo_uno}")

total = parcial1 | parcial2
print(f"Aprobaron al menos un parcial: {total}")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos = {'manzanas': 3, 'bananas': 8, 'peras': 12, 'anana': 2}
print("Los productos ingreados son: ")
for i in productos:
    print(i)
menu = [
    "1. Consutlar stock de un producto ingresado",
    "2. Agregar stock a productos existentes",
    "3. Agregar un nuevo producto",
    "0. Salir"
]
while True:
    print("--- Menu ---")
    for opcion in menu:
        print(opcion)
    
    seleccion = input("Seleccione una opcion: ").strip()
    
    if seleccion == "1":
        print("Los productos ingreados son: ")
        for i in productos:
            print(i)
        consulta = input("Ingrese el nombre del producto que quiere consultar: ").strip().lower()
        if consulta in productos:
            print(f"El producto {consulta} tiene {productos[consulta]} unidades de stock")

    elif seleccion == "2":
        print("Los productos ingreados son: ")
        for i in productos:
            print(i)
        agregar_stock = input("Ingrese el nombre del producto que desea agregar stock: ").strip().lower()
        if agregar_stock in productos:
            stock = int(input(f"Ingrese la cantidad de stock que desea agregar de {agregar_stock}: "))
            if stock >= 0: 
                productos[agregar_stock] += stock
                print(f"Stock actualizado, ahora {agregar_stock} tiene {productos[agregar_stock]} unidades.")
            else:
                print("Entrada inválida")
        else:
            print("El nombre ingresado no se encuentra en la lista de productos!")
            continue
    
    elif seleccion == "3":
        print("Los productos ingreados son: ")
        for i in productos:
            print(i)
        producto_nuevo = input("Ingrese el producto que desea agregar: ").strip().lower()
        if producto_nuevo in productos:
            print("El producto ingresado ya existe dentro de la lista de productos.")
            continue
        else:
            productos[producto_nuevo] = 0
            print ("Producto agregado correctamente!")
            print(productos)
    
    elif seleccion == "0":
        break

    else:
        print("Entrada inválida, vuelva a intntarlo!")


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.


agenda = {
    ("lunes", "16:00"): "Clase Matemática",
    ("martes", "12:00"): "Gimnasio",
    ("miercoles", "8:00"): "Clase inglés",
    ("jueves", "10:00"): "Turno dentista",
    ("viernes", "21:00"): "Cumpleaños Lautaro"
}

dia = input("Ingrese el dia: ").strip().lower()
hora = input("Ingrese la hora (ej: 16:00): ").strip()
evento = agenda.get((dia, hora))

if evento:
    print(f"Actividad el dia {dia} a las {hora}: {evento}")
else:
    print("No hay actividad en la agenda para ese dia y hora.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises_original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Peru":"Lima"}

print("Paises original:")
for pais, capital in paises_original.items():
    print(f"{pais}, {capital}")

paises_invertido = {capital: pais for pais, capital in paises_original.items()}

print("Paises invertidos:")
for capital, pais in paises_invertido.items():
    print(f"{capital}, {pais}")