
from conector import Conector
from ingreso import Ingreso

ingreso = Ingreso()
conector = Conector()

class Principal():
    
    def menu(self):
        while True:
            print("""
                            █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                            █           REGISTRO DE USUARIOS          █
                            █                                         █
                            █    1) Listar                            █
                            █    2) Agregar                           █
                            █    3) Modificar                         █
                            █    4) Eliminar                          █
                            █                                         █
                            █    INGRESE '0' PARA SALIR               █
                            █                                         █
                            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """)
            opcion = int(input("Ingrese su opción: "))

            if opcion < 0 and opcion > 5:
                print("Opción no válida")
            elif opcion == 0:
                exit()
            else:
                self.opciones(opcion)

    def opciones(self, op):
        if op == 1:
            try:
                listado = conector.listar() 
                #print(listado)
                if len(listado) > 0:
                    #print(listado)
                    ingreso.listarU(listado)
                else:
                    print('No hay registro de usuarios')
            except:
                print('Ocurrió un error en el listado')
        if op == 2:
            registro = ingreso.agregar()
            try:
                conector.registro(registro)
            except:
                print('Ocurrió un error en agregar')
        if op == 3:
            try:
                usuario = conector.listar()
                if len(usuario) > 0:
                    usuarioA = ingreso.actualizar(usuario)
                    print(usuarioA)
                    if usuarioA:
                        conector.actualizar(usuarioA)
                    else:
                        print("Usuario no encontrado")
                else:
                    print("Base de Datos vacía")
            except:
                print('Ocurrió un error en agregar')
        if op == 4:
            try:
                usuario = conector.listar()
                if len(usuario) > 0:
                    usuarioE = ingreso.eliminar(usuario)
                    if not (usuarioE == ""):
                        conector.eliminar(usuarioE)
                    else:
                        print('Usuario no encontrado')
                else:
                    print('Base de Datos vacía')
            except:
                print('Ocurrió un error en eliminar')

principal = Principal()
principal.menu()
            
                