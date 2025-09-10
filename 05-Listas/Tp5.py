#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas = [8, 7, 4, 10, 5, 8.5, 7.5, 3, 6, 6.5]

for i in range (0, 10):
    print(notas[i])

prom_cont = 0
for nota in notas:
    prom_cont += nota
print ("El promedio de las notas es de ", prom_cont / 10)
nota__mas_alta = max(notas)
nota_mas_baja = min (notas)
print (f"La nota mas alta fue: {nota__mas_alta} y la nota mas baja fue: {nota_mas_baja} ")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for x in range (0, 5):
    productos.append(input("Ingrese un producto: "))

productos_sorted = sorted(productos)
for y in range (0, 5):
    print(productos_sorted[y])

borrar = input("Desea borrar un producto? Ingrese el nombre del producto que desea borrar, de lo contrario presione N")

if borrar in productos:
    productos.remove(borrar)
    for b in range (0, 4):
        print(productos[b])
else:
    pass

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random

lista_par = []
lista_impar = []
contador_par = 0
contador_impar = 0

for a in range (0,15):
    numero_azar = random.randint(0, 100)
    if numero_azar % 2 == 0:
        lista_par.append(numero_azar)
        contador_par += 1
    else:
        lista_impar.append(numero_azar)
        contador_impar += 1

print("Lista par", lista_par, "hay", contador_par, "numeros pares")
print ("Lista impar", lista_impar, "hay", contador_impar, "numeros impares")


#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetir = list(set(datos))
print("La nueva lista es: ", datos_sin_repetir)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

presentes = ["Agustin", "Francisco", "Celeste", "Franco", "Martina", "Matias", "Gaspar", "Sergio"]

print ("El listado de alumnos presentes es: ", presentes)
continuar = input("Si desea agregar un alumno presione A, si desea eliminar un alumno presione E, si desea continuar presione cualquier otra tecla ")


if continuar == "A" or continuar == "a":
    presentes.append(input("Ingrese el nombre que desea agregar: "))
elif continuar == "E" or continuar == "e":
    presentes.remove(input("Ingrese el nombre que desea elminar: "))
else:
    pass

print("El listado de alumnos presentes es: ", presentes)

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

num_siete = [3, 8, 9, 11, 32, 55, 2]

for i in range (0, 7):
    num_siete[0] = num_siete [1]
    num_siete[1] = num_siete [2]
    num_siete[2] = num_siete [3]
    num_siete[3] = num_siete [4]
    num_siete[4] = num_siete [5]
    num_siete[5] = num_siete [0]
    
print (num_siete)



