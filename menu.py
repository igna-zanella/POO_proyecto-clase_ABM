
from datos import Dato

class Menu():

    def menu(self):
        ingreso = Dato()
        

        while True:

            print('\033[92m' + """
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
            """ + '\033[0m')
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                ingreso.agregar()
                print('\033[92m' + "agregado 👌" + '\033[0m')
            elif opcion == "2":
                ingreso.listar()
                print('\033[92m' + "mostrado ✨" + '\033[0m')
            elif opcion == "3":
                ingreso.buscar()
                print('\033[92m' + "encontrado 😎" + '\033[0m')
            elif opcion == "4":
                while True:
                    print('\033[92m' + """
        ╔═════════════════════════════════════════╗
        ║                                         ║
        ║                 EDITAR                  ║
        ║                                         ║                               
        ║   1) Datos personales                   ║
        ║   2) Saldo                              ║
        ║   3) Volver                             ║
        ║                                         ║
        ╚═════════════════════════════════════════╝ 
                        """ + '\033[0m')
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
                        print('\033[31m' + opcionEditar + " no es una opción válida " + '\033[0m' + "😦")
                if opcionEditar == "1" or opcionEditar == "2":    
                    print('\033[92m' + "editado ✔" + '\033[0m')
                else:
                    print("Ha vuelto al menú principal")
            elif opcion == "5":
                ingreso.buscarHistorial()
                print('\033[92m' + "Historial 📁" + '\033[0m')
            elif opcion == "6":
                ingreso.eliminar()
                print('\033[92m' + "eliminado 😢" + '\033[0m')
            elif opcion == "0":
                print('\033[92m' + "Gracias por su visita 😉" +'\033[0m')
                exit()
            else:
                print('\033[31m' + opcion + " no es una opción válida " + '\033[0m' + "😦")

menu_01 = Menu()

menu_01.menu()

#TAREA, EDITAR EL NOMBRE Y APELLIDO, Y SALDO DEL USUARIO. Se complica cuando se guarda el historial y el resto. Modificar el objeto en si.