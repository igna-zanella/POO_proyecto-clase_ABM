
class Col:
    negro = '\033[30m'
    rojo = '\033[31m'
    verde = '\033[32m'
    amarillo = '\033[33m'
    blanco = '\033[37m'
    finColor = '\033[39m'

class Ingreso:
    def listarU(self, usuario):
        for usu in usuario:
            data = 'Nombre: {0} \nApellido: {1}\nDNI: {2}\n'
            print(data.format(usu[0], usu[1], usu[2]))

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
                direccion = int(input(Col.amarillo + "Dirección: " + Col.finColor))
                break
            except ValueError:
                print(Col.rojo + "El valor debe ser numérico." + Col.finColor)

        usuario = (dni, nombre, apellido, direccion)
        return usuario
    
    def modificar(self):
        print(Col.verde + "EDITAR USUARIO" + Col.finColor)
        dni = input("Ingrese el DNI: ")
        for usu in usuario[3]:
            if dni == usu:
                print(Col.verde + "INGRESE SUS DATOS" + Col.finColor)

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

        usuario = (dni, nombre, apellido)
        return usuario