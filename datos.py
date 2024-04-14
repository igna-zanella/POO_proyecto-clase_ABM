
from usuario import Persona

listaUsuario = []

class Dato():
    def agregar(self):
        print("INGRESE SUS DATOS")
        dniCorrecto = False
        while not dniCorrecto:
            dni = input('\033[33m' + "DNI: "+ '\033[0m')
            if len(dni)==8:
                if dni.isnumeric():
                    dniCorrecto = True
                else:
                    print("Debe ser numérico")
            else:
                print("Debe ser contener 8 dígitos")

        nombreC = False
        while not nombreC:                
            nombre = input('\033[33m' + "Nombre: "+ '\033[0m').capitalize()
            if nombre.isalpha():
                if len(nombre) <= 18 and len(nombre)>=3:
                    nombreC = True
                else:
                    print("El nombre debe ser entre 3 y 18 letras.")
            else:    
                print("Solo se aceptan letras. Vuelva a intentarlo.")

        while True:                
            apellido = input('\033[33m' + "apellido: "+ '\033[0m').capitalize()
            if apellido.isalpha():
                if len(apellido) <= 18 and len(apellido)>=3:
                    break
                else:
                    print("El nombre debe ser entre 3 y 18 letras.")
            else:    
                print("Solo se aceptan letras. Vuelva a intentarlo.")

        while True:
            try:
                deposito = float(input('\033[33m' + "Depósito: " + '\033[0m'))
                break
            except ValueError:
                print("El valor debe ser numérico.")

        while True:
            try:
                retiro = float(input('\033[33m' + "Retiro: " + '\033[0m'))
            except:
                print("El valor debe ser numérico.")
            else:
                break     

        usario = Persona(dni, nombre, apellido, deposito, retiro)
        listaUsuario.append(usario)

    def listar(self):
        print("LISTA DE USUARIOS")
        for objeto in listaUsuario:
            objeto.imprimir()

    def buscar(self):
        print("BÚSQUEDA POR DNI")
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                objeto.imprimir()
            #probar con else para dni no encontrado.

    def editarSaldo(self):
        print("EDITAR SALDO")
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                deposito = float(input('\033[33m' + "Depósito: " + '\033[0m'))
                retiro = float(input('\033[33m' + "Retiro: " + '\033[0m'))
                #probar validación de los float con while True Try/except
                objeto.editarSaldo(deposito, retiro)
                objeto.imprimir()
                modificado = objeto.modificaciones(deposito,retiro)
                objeto.historial.append(modificado)

    def editarNombre(self):
        print("EDITAR NOMBRE")
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                nombre = input('\033[33m' + "Nuevo nombre: " + '\033[0m')
                apellido = input('\033[33m' + "Nuevo apellido: " + '\033[0m')
                objeto.editarNombre(nombre, apellido)
                objeto.imprimir()
            else:
                print("DNI no encontrado")

    def buscarHistorial(self):
        print("HISTORIAL DE USUARIO")
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                print("HISTORIAL:")
                for mensaje in objeto.historial:
                    print(f'{mensaje}')
                    #puede incluir la fecha de cada movimiento. "Historial" arriba del for.

    def eliminar(self):
        print("ELIMINAR USUARIO")
        dni = input("Ingrese el DNI: ")
        for objeto in listaUsuario:
            if dni == objeto.dni:
                listaUsuario.remove(objeto)
    
    