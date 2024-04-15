
from datos import Dato

class Col:
    negro = '\033[30m'
    rojo = '\033[31m'
    verde = '\033[32m'
    amarillo = '\033[33m'
    blanco = '\033[37m'
    finColor = '\033[39m'
class Menu():

    def menu(self):
        ingreso = Dato()

        while True:

            print(Col.verde + """
        ╔═════════════════════════════════════════╗
        ║                                         ║
        ║           REGISTRO DE USUARIOS          ║
        ║                                         ║
        ║    1) Agregar                           ║
        ║    2) Mostrar                           ║
        ║    3) Buscar                            ║
        ║    4) Editar                            ║
        ║    5) Historial                         ║
        ║    6) Eliminar                          ║
        ║                                         ║
        ║    INGRESE '0' PARA SALIR               ║
        ║                                         ║
        ╚═════════════════════════════════════════╝    
            """ + Col.finColor)
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                ingreso.agregar()
                print(Col.verde + "agregado 👌" + Col.finColor)
            elif opcion == "2":
                ingreso.listar()
                print(Col.verde + "mostrado ✨" + Col.finColor)
            elif opcion == "3":
                ingreso.buscar()
                print(Col.verde + "encontrado 😎" + Col.finColor)
            elif opcion == "4":
                while True:
                    print(Col.verde + """
        ╔═════════════════════════════════════════╗
        ║                                         ║
        ║                 EDITAR                  ║
        ║                                         ║                               
        ║   1) Datos personales                   ║
        ║   2) Saldo                              ║
        ║   3) Volver                             ║
        ║                                         ║
        ╚═════════════════════════════════════════╝ 
                        """ + Col.finColor)
                    opcionEditar = input("Elija la opción a editar: ")
                    if opcionEditar == "1":
                        ingreso.editarNombre()
                        break
                    elif opcionEditar == "2":
                        ingreso.editarSaldo()
                        break
                    elif opcionEditar == "3":
                        break
                    else:
                        print(Col.rojo + opcionEditar + " no es una opción válida " + Col.finColor + "😦")
                if opcionEditar == "1" or opcionEditar == "2":    
                    print(Col.verde + "editado ✔" + Col.finColor)
                else:
                    print(Col.amarillo + "Ha vuelto al menú principal ⬅" + Col.finColor)
            elif opcion == "5":
                ingreso.buscarHistorial()
                print(Col.verde + "Historial 📁" + Col.finColor)
            elif opcion == "6":
                ingreso.eliminar()
                print(Col.verde + "eliminado ❌" + Col.finColor)
            elif opcion == "0":
                print(Col.verde + "Gracias por su visita 😉" +'\033[0m')
                exit()
            else:
                print(Col.rojo + opcion + " no es una opción válida " + Col.finColor + "😦")

menu_01 = Menu()

menu_01.menu()

#TAREA, EDITAR EL NOMBRE Y APELLIDO, Y SALDO DEL USUARIO. Se complica cuando se guarda el historial y el resto. Modificar el objeto en si.