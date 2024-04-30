
class Ingreso:
    def listarU(self, usuario):
        for usu in usuario:
            data = 'Nombre: {0} \nApellido: {1}\n'
            print(data.format(usu[0], usu[1]))
