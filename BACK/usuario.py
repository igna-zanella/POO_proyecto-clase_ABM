
class Persona():
    def __init__(self, dni, nombre, apellido, deposito, retiro):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.deposito = deposito
        self.retiro = retiro
        self.saldo = (deposito - retiro)
        self.historial = []

    def imprimir(self):
        print(f'''
            DATOS DEL USUARIO
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Depósito: {self.deposito}
            Retiro: {self.retiro}
            Saldo: {self.saldo}''')
    
    def editarSaldo(self, deposito, retiro):
        self.deposito += deposito
        self.retiro += retiro
        self.saldo += deposito - retiro
    
    def editarNombre(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def modificaciones(self, deposito, retiro):
        return f'\nDepósito: {deposito} \nRetiro: {retiro}'
    
    