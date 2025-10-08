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
