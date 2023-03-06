
import helpers
import database as db


def iniciar():

# Inicializa el menu
  while True:
    helpers.clear()

    print("===============================")
    print(" Gestor de Vehiculos v1.0.0    ")
    print("===============================")
    print(" [1]. Listar Vehiculos         ")
    print(" [2]. Mostrar Vehiculo           ")
    print(" [3]. Añadir Vehiculo            ")
    print(" [4]. Modificar Vehiculo         ")
    print(" [5]. Eliminar Vehiculo        ")
    print(" [6]. Salir")
    print("===============================")

    opcion = input("Seleccione una opcion: ")
    helpers.clear()

    if opcion == '1':
            print("Listando vehículos...\n")
            for vehiculo in db.vehiculos.lista:
                print(vehiculo)

    if opcion == '2':
            print("Buscando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            vehiculo = db.vehiculos.buscar(matricula)
            print(vehiculo) if vehiculo else print("vehículo no encontrado.")

    if opcion == '3':
            print("Añadiendo vehículo...\n")
            matricula = None
            while True:
                matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
                if helpers.matricula_valida(matricula, db.vehiculos.lista):
                    break
            color = helpers.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
            ruedas = helpers.leer_texto(2, 30, "Ruedas (de 2 a 30 chars)").capitalize()
            db.vehiculos.crear(matricula, color, ruedas)
            print("Vehículo añadido correctamente.")

    if opcion == '4':
            print("Modificando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            vehiculo = db.vehiculos.buscar(matricula)
            if vehiculo:
                color = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{vehiculo.color}]").capitalize()
                ruedas = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars) [{vehiculo.ruedas}]").capitalize()
                db.vehiculos.modificar(vehiculo.matricula, color, ruedas)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

    if opcion == '5':
            print("Eliminando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            print("Vehículo borrado correctamente.") if db.vehiculos.borrar(
                matricula) else print("Vehículo no encontrado.")
            
    if opcion == '6':
            print("Saliendo...\n")
            
    if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5' and opcion != '6':
            print("Opción inválida. Introduzca una opción válida.\n")


    input("\nPresiona ENTER para continuar...")




