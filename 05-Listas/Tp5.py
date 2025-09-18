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

num_siete = [num_siete[-1]] + num_siete[:-1]

print(num_siete)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica. 

temp_semanal = [
    [16.7, 23],
    [18, 25.5],
    [17.8, 22],
    [14.2, 18.2],
    [12, 17.7],
    [12.3, 16],
    [13, 18.9]
]

suma_min = 0
suma_max = 0

for dia in temp_semanal:
    suma_min += dia [0]
    suma_max += dia [1]

prom_min = suma_min / len(temp_semanal)
prom_max = suma_max / len(temp_semanal)

print("El promedio de temperaturas máximas es: ", round(prom_max, 2), "C°")
print("El promedio de temperaturas minimas es: ", round(prom_min, 2), "C°")

amplitudes = []

for dia in temp_semanal:
    amplitudes.append(dia[1] - dia[0])

mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1

print ("Mayor amplitud termica: ", mayor_amplitud,"C° en el dia", dia_mayor)


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

notas_materias = [
    [9, 8, 10], 
    [6, 7, 6], 
    [4,7,3], 
    [9, 9, 8], 
    [7, 8, 6]
]


for i, alumnos in enumerate(notas_materias, start=1):
    prom = sum(alumnos)
    print("El promedio del alumno",i, round(prom / 3, 2))

materia1 = 0
materia2 = 0
materia3 = 0

for promedio_materias in notas_materias:
    materia1 += promedio_materias[0]
    materia2 += promedio_materias[1]
    materia3 += promedio_materias[2]

print ("Para la materia 1 el promedio es: ", materia1 / len(notas_materias))
print ("Para la materia 2 el promedio es: ", materia2 / len(notas_materias))
print ("Para la materia 3 el promedio es: ", materia3 / len(notas_materias))



#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 

tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

for i in tateti:
    print(i)

for jugadas in range (0,3):

    fila1 = int(input("JUGADOR 1: Ingrese la fila en la que quiere colocar la X!(1 - 2 - 3)"))
    columna1 = int(input("JUGADOR 1: Ahora ingrese la columna!(1 - 2 - 3)"))

    if fila1 == 1:
        if columna1 == 1:
            tateti[0][0] = "X"
        elif columna1 == 2:
            tateti[0][1] = "X"
        elif columna1 == 3:
            tateti[0][2] = "X"
    elif fila1 == 2:
        if columna1 == 1:
            tateti[1][0] = "X"
        elif columna1 == 2:
            tateti[1][1] = "X"
        elif columna1 == 3:
            tateti[1][2] = "X"
    elif fila1 == 3:
        if columna1 == 1:
            tateti[2][0] = "X"
        elif columna1 == 2:
            tateti[2][1] = "X"
        elif columna1 == 3:
            tateti[2][2] = "X"
    else:
        break



    for i in tateti:
        print(i)

    fila2 = int(input("JUGADOR 2: Ingrese la fila en la que quiere colocar la O!(1 - 2 - 3)"))
    columna2 = int(input("JUGADOR 2: Ahora ingrese la columna!(1 - 2 - 3)"))

    if fila2 == 1:
        if columna2 == 1:
            tateti[0][0] = "O"
        elif columna2 == 2:
            tateti[0][1] = "O"
        elif columna2 == 3:
            tateti[0][2] = "O"
    elif fila2 == 2:
        if columna2 == 1:
            tateti[1][0] = "O"
        elif columna2 == 2:
            tateti[1][1] = "O"
        elif columna2 == 3:
            tateti[1][2] = "O"
    elif fila2 == 3:
        if columna2 == 1:
            tateti[2][0] = "O"
        elif columna2 == 2:
            tateti[2][1] = "O"
        elif columna2 == 3:
            tateti[2][2] = "O"
    else:
        break

    for i in tateti:
        print(i)

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

tienda = [
    [3, 10, 2, 1],
    [5, 1, 1, 3],
    [12, 3, 3, 9],
    [7, 9, 6, 11],
    [2, 2, 7, 2],
    [3, 15, 19, 4],
    [0, 3, 11, 8]
]

manzanas = 0
cocacola = 0
papas_fritas = 0
alfajor = 0


for total in tienda:
    manzanas += total[0]
    cocacola += total[1]
    papas_fritas += total[2]
    alfajor += total[3]

print(f"El total de manzanas vendidas es de {manzanas}, el total de Coca Cola vendidas es de {cocacola}, el total de papas fritas vendidas es de {papas_fritas} y el total de alfajores vendidos es de {alfajor}")

ventas_total = []

for i, totaldia in enumerate (tienda, start=1):
    total_diario = sum(totaldia)
    ventas_total.append((i, total_diario))

dia_max, venta_max = max(ventas_total, key=lambda x: x[1])
print(f"El dia con mas ventas fue el {dia_max} con {venta_max} ventas.")

productos = {
    "manzanas": manzanas,
    "cocacola": cocacola,
    "papas fritas": papas_fritas,
    "alfajor": alfajor
}

mas_vendido = max(productos, key=productos.get)
print(f"El producto más vendido en la semana fue {mas_vendido} con {productos[mas_vendido]} ventas")




