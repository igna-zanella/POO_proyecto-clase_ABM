
from usuario import Persona

class Contacto(Persona):
    def __init__(self, dni, nombre, apellido, deposito, retiro, email, telefono):
        super().__init__(dni, nombre, apellido, deposito, retiro)
        self.email = email
        self.telefono = telefono
        
    def imprimir(self):
        return super().imprimir() + f'''
            Teléfono: {self.telefono}
            Email: {self.email}
            '''