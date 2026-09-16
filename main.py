from paciente import Paciente

def main():
    # Crear paciente con el constructor __init__
    p1 = Paciente("11.111.111-1", "Pablo Ferrada", 40, "Isapre")
    # Mostrar informacion del paciente
    # __str__es llamado automaticamente al imprimir el objeto
    print(p1)

if __name__ == "__main__":
    main()