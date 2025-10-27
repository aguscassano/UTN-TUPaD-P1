#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

archivo_productos = open("productos.txt", "w")
archivo_productos.write("Manzana,200,9\n")
archivo_productos.write("Banana,400,5\n")
archivo_productos.write("Pera,700,12\n")
archivo_productos.close()

archivo_productos = open ("productos.txt", "r")
contenido = archivo_productos.read()
print(contenido)
archivo_productos.close()


#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30


with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        
        if linea_limpia:
            partes = linea_limpia.split(",")

            if len(partes) == 3:
                nombre = partes [0]
                precio = partes [1]
                cantidad = partes [2]

                print(f"Producto= {nombre} | Precio= ${precio} | Cantidad= {cantidad}")
            else:
                print("Formato incorrecto.")


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("Ingrese un nuevo producto")
nuevo_producto = input("Ingrese el nombre del producto que desea agregar: ")
nuevo_precio = float(input("Ingrese el precio del producto: "))
nueva_cantidad = int(input("Ingrese la cantidad de stock del producto: "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_producto},{nuevo_precio},{nueva_cantidad}\n")

print(f"El producot {nuevo_producto}, se agrego exitosamente!")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        
        if linea_limpia:
            partes = linea_limpia.split(",")

            if len(partes) == 3:
                nombre = partes [0]
                precio = partes [1]
                cantidad = partes [2]

                print(f"Producto= {nombre} | Precio= ${precio} | Cantidad= {cantidad}")
            else:
                print("Formato incorrecto.")


#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.

lista_productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()

        if linea_limpia:
            partes = linea_limpia.split(",")

            if len(partes) == 3:
                nombre = partes [0]
                precio = partes [1]
                cantidad = partes [2]

                producto_dic = {
                    "Nombre": nombre,
                    "Precio": precio,
                    "Cantidad": cantidad
                }

                lista_productos.append(producto_dic)
            else:
                print("Linea ignoradad, formato incorrecto")

print("Contenido de la lista de diccionarios: ")
for producto in lista_productos:
    print(producto)


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.


nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")

producto_encontrado = False

for producto in lista_productos:
    if producto["Nombre"].lower() == nombre_buscado.lower():
        print("Producto encontrado!")
        print(f"Nombre= {producto["Nombre"]}")
        print(f"Precio= ${producto["Precio"]}")
        print(f"Cantidad= {producto["Cantidad"]}")

        producto_encontrado = True

        break

if not producto_encontrado:
    print(f"Error! El producto {nombre_buscado}, no se encuentra en el inventario.")



#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista.


with open("productos.txt", "w") as archivo_salida:

    for producto in lista_productos:
        nombre = producto["Nombre"]
        precio = producto["Precio"]
        cantidad = producto["Cantidad"]

        linea_nueva = f"{nombre},{precio},{cantidad}\n"

        archivo_salida.write(linea_nueva)

print("Archivo guardado correctamente!")
with open("productos.txt", "r") as archivo:
    print(archivo.read())