from paciente import Paciente
pacientes: list[Paciente] = []

from departamento import Departamento
departamentos: list[Departamento] = []

def agregar_paciente()->None:
    #Crear in objeto manualmente con atributos
    rut = input("Ingrese el RUT del paciente: ")
    nombre = input("Ingrese eñ nombre del paciente: ")
    edad = int(input("Ingrese la edad el paciente: "))
    print("Previsiones disponibles")
    print("1.-Fonasa")
    print("2.-Isapre")
    prevision = input("Seleccione la prevision del paciente: ")
    if prevision == "1":
        prevision = "Fonasa"
    else:
        prevision = "Isapre"
    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un munero valido.")

def menu()->int:
    opcion=-1
    while opcion<0 or opcion>6:
        print("Menu de clinica")
        print("1.- Agregar paciete")
        print("2.- Editar paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir un paciente")
        print("5.- Imprimir todos los pacientes")
        print("6.-Menu de departamentos")
        print("0.- salir")
        opcion = int(input("Seleccione una opcion: "))
    return opcion

def buscar_paciente()->Paciente:
    rut = input("Ingtrese el R.U.T. del paciente abuscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
        return None

def imprimir_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("Paciente no encontrado.")

def imprimir_pacientes()->None:
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("Menu de edicion de paciente")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar prevision")
        opcion = leer_numero("Seleccione una opcion: ")
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            paciente.nombre = nuevo_nombre
        elif opcion == 2:
            nueva_edad = leer_numero("ingrese la nueva edad: ")
            paciente.edad = nueva_edad
        elif opcion == 3:
            print("Previsiones disponibles: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("0.- No hacer cambios")
            nueva_prevision = input("Seleccione la nueva prevision: ")
            if nueva_prevision == "1":
                paciente.prevision = "Fonasa"
            elif nueva_prevision == "2":
                paciente.prevision = "Isapre"
            else:
                print("No se realizaron cambios en la prevision")
    else:
        print("paciente no encontrado.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        paciente.remove(paciente)
        print("Paciente eliminado exitosamente.")
    else:
        print("Paciente no encontrado.")

def menu_departamentos()->int:
    opcion2=-1
    while opcion2<0 or opcion2>5:
        print("Menu de departamentos")
        print("1.- Agregar departamento")
        print("2.- Editar departamento")
        print("3.- Eliminar departamento")
        print("4.- Imprimir un departamento")
        print("5.- Imprimir todos los departamentos")
        print("0.- salir")
        opcion2 = int(input("Seleccione una opcion: "))
    return opcion2

def agregar_departamento()->None:
    nombre = input("Ingrese el nombre del departamento: ")
    cantidad_camas = leer_numero("Ingrese la cantidad de camas del departamento: ")
    pacientes_departamento = []
    departamento = Departamento(nombre, cantidad_camas, pacientes_departamento)
    departamentos.append(departamento)
    print("Departamento agregado exitosamente.")

def editar_departamento()->None:
    nombre = input("Ingrese el nombre del departamento a editar: ")
    for departamento in departamentos:
        if departamento.nombre == nombre:
            print("Menu de edicion de departamento")
            print("1.- Editar nombre")
            print("2.- Editar cantidad de camas")
            print("3.- Agregar paciente al departamento")
            print("4.- Eliminar paciente del departamento")
            opcion = leer_numero("Seleccione una opcion: ")
            if opcion == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                departamento.nombre = nuevo_nombre
            elif opcion == 2:
                nueva_cantidad_camas = leer_numero("Ingrese la nueva cantidad de camas: ")
                departamento.cantidad_camas = nueva_cantidad_camas
            elif opcion == 3:
                paciente = buscar_paciente()
                if paciente:
                    departamento.pacientes.append(paciente)
                    print("Paciente agregado al departamento.")
                else:
                    print("Paciente no encontrado.")
            elif opcion == 4:
                paciente = buscar_paciente()
                if paciente and paciente in departamento.pacientes:
                    departamento.pacientes.remove(paciente)
                    print("Paciente eliminado del departamento.")
                else:
                    print("Paciente no encontrado en el departamento.")
            return
    print("Departamento no encontrado.")



def main():
    op=-1
    while op!=0:
        op=menu()
        if op==1:
            print("Agregar paciente")
            agregar_paciente()
        elif op==2:
            print("Editando paciente")
            editar_paciente()
        elif op==3:
            print("Eliminando paciente")
            eliminar_paciente()
        elif op==4:
            print("Imprimiendo un paciente")
            imprimir_paciente()
        elif op==5:
            print("Imprimiendo todos los pacientes")
            imprimir_pacientes()
        elif op==6:
            print("Menu de departamentos")
            menu_departamentos()
        elif op==0:
            print("Saliendo del programa")

if __name__ == "__main__":
    main()