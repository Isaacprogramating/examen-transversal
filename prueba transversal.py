import random
import statistics
import math
import csv

# Lista de empleados
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para asignar sueldos aleatorios
def asignar_sueldos(trabajadores):
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    bajos = {k: v for k, v in sueldos.items(2) if v < 800000}
    medios = {k: v for k, v in sueldos.items(2) if 800000 <= v <= 2000000}
    altos = {k: v for k, v in sueldos.items(1) if v > 2000000}
    return bajos, medios, altos

# Función para ver estadísticas
def ver_estadisticas(sueldos):
    sueldos_lista = list(sueldos.values())
    sueldo_max = max(sueldos_lista)
    sueldo_min = min(sueldos_lista)
    promedio = statistics.mean(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(x) for x in sueldos_lista) / len(sueldos_lista))
    return sueldo_max, sueldo_min, promedio, media_geometrica

# Función para generar el reporte de sueldos
def reporte_sueldos(sueldos):
    reporte = []
    for trabajador, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte.append([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    return reporte

# Función para exportar el reporte a un archivo CSV
def exportar_csv(reporte, filename='reporte_sueldos.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)

# Función del menú principal
def menu():
    sueldos = {}
    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = asignar_sueldos(trabajadores)
            print("Sueldos asignados.")
        elif opcion == '2':
            if not sueldos:
                print("Debe asignar sueldos primero.")
            else:
                bajos, medios, altos = clasificar_sueldos(sueldos)
                print("\nSueldos clasificados:")
                print(f"Sueldos menores a $800.000: {bajos}")
                print(f"Sueldos entre $800.000 y $2.000.000: {medios}")
                print(f"Sueldos superiores a $2.000.000: {altos}")
        elif opcion == '3':
            if not sueldos:
                print("Debe asignar sueldos primero.")
            else:
                sueldo_max, sueldo_min, promedio, media_geometrica = ver_estadisticas(sueldos)
                print("\nEstadísticas:")
                print(f"Sueldo más alto: {sueldo_max}")
                print(f"Sueldo más bajo: {sueldo_min}")
                print(f"Promedio de sueldos: {promedio}")
                print(f"Media geométrica de sueldos: {media_geometrica}")
        elif opcion == '4':
            if not sueldos:
                print("Debe asignar sueldos primero.")
            else:
                reporte = reporte_sueldos(sueldos)
                exportar_csv(reporte)
                print("Reporte de sueldos generado y exportado a CSV.")
        elif opcion == '5':
            print("Finalizando programa…")
            print("Desarrollado por Franco ruz RUT 21.843.711-7")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú principal
menu()