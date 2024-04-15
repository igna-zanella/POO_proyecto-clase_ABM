
from usuario import Persona

class Col:
    negro = '\033[30m'
    rojo = '\033[31m'
    verde = '\033[32m'
    amarillo = '\033[33m'
    blanco = '\033[37m'
    finColor = '\033[39m'

listaUsuario = []

class Dato():
    def agregar(self):
        print(Col.verde + "INGRESE SUS DATOS" + Col.finColor)
        dniCorrecto = False
        while not dniCorrecto:
            dni = input('\033[33m' + "DNI: " + '\033[39m')
            if len(dni)==8:
                if dni.isnumeric():
                    dniCorrecto = True
                else:
                    print("Debe ser numérico")
            else:
                print("Debe ser contener 8 dígitos")

        nombreC = False
        while not nombreC:                
            nombre = input(Col.amarillo + "Nombre: " + Col.finColor).capitalize()
            if nombre.isalpha():
                if len(nombre) <= 18 and len(nombre)>=3:
                    nombreC = True
                else:
                    print("El nombre debe ser entre 3 y 18 letras.")
            else:    
                print("Solo se aceptan letras. Vuelva a intentarlo.")

        while True:                
            apellido = input(Col.amarillo + "Apellido: " + Col.finColor).capitalize()
            if apellido.isalpha():
                if len(apellido) <= 18 and len(apellido)>=3:
                    break
                else:
                    print("El nombre debe ser entre 3 y 18 letras.")
            else:    
                print("Solo se aceptan letras. Vuelva a intentarlo.")

        while True:
            try:
                deposito = float(input(Col.amarillo + "Depósito: " + Col.finColor))
                break
            except ValueError:
                print(Col.rojo + "El valor debe ser numérico." + Col.finColor)

        while True:
            try:
                retiro = float(input(Col.amarillo + "Retiro: " + Col.finColor))
            except:
                print(Col.rojo + "El valor debe ser numérico." + Col.finColor)
            else:
                break     

        usario = Persona(dni, nombre, apellido, deposito, retiro)
        listaUsuario.append(usario)

    def listar(self):
        print(Col.verde + "LISTA DE USUARIOS" + Col.finColor)
        for objeto in listaUsuario:
            objeto.imprimir()

    def buscar(self):
        print(Col.verde + "BÚSQUEDA POR DNI" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                objeto.imprimir()
            else:
                print(Col.rojo + "DNI no encontrado ⛔" + Col.finColor)
            #probar con else para dni no encontrado.

    def editarSaldo(self):
        print(Col.verde + "EDITAR SALDO" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                # deposito = float(input(Col.amarillo + "Depósito: " + Col.finColor))
                while True:
                    try:
                        deposito = float(input(Col.amarillo + "Depósito: " + Col.finColor))
                        break
                    except ValueError:
                        print(Col.rojo + "El valor debe ser numérico." + Col.finColor)
                while True:
                    try:
                        retiro = float(input(Col.amarillo + "Retiro: " + Col.finColor))
                        break
                    except ValueError:
                        print(Col.rojo + "El valor debe ser numérico." + Col.finColor)
                # retiro = float(input(Col.amarillo + "Retiro: " + Col.finColor))
                objeto.editarSaldo(deposito, retiro)
                objeto.imprimir()
                modificado = objeto.modificaciones(deposito,retiro)
                objeto.historial.append(modificado)
            else:
                print(Col.rojo + "DNI no encontrado ⛔" + Col.finColor)

    def editarNombre(self):
        print(Col.verde + "EDITAR NOMBRE" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                nombre = input(Col.amarillo + "Nuevo nombre: " + Col.finColor)
                apellido = input(Col.amarillo + "Nuevo apellido: " + Col.finColor)
                objeto.editarNombre(nombre, apellido)
                objeto.imprimir()
            else:
                print(Col.rojo + "DNI no encontrado ⛔" + Col.finColor)

    def buscarHistorial(self):
        print(Col.verde + "HISTORIAL DE USUARIO" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                print("HISTORIAL:")
                for mensaje in objeto.historial:
                    print(f'{mensaje}')
            else:
                print(Col.rojo + "DNI no encontrado ⛔" + Col.finColor)
                #puede incluir la fecha de cada movimiento. "Historial" arriba del for.

    def eliminar(self):
        print(Col.verde + "ELIMINAR USUARIO" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                listaUsuario.remove(objeto)
            else:
                print(Col.rojo + "DNI no encontrado ⛔" + Col.finColor)
    
    