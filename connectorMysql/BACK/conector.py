
from mysql.connector import Error
import mysql.connector

class Conector():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                database = '2304'
            )
        except Error as res:
            print(f'No se pudo establecer la conexión: {res}')

    def listar(self):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                #cur.execute('select * from usuario')
                cur.execute('select usuario.nombre, usuario.apellido, direccion.calle, direccion.numero, direccion.codigoP from usuario, direccion where usuario.direccion = direccion.id')
                respuesta = cur.fetchall()
                return respuesta
            except Error as res:
                print(f'No se pudo listar: {res}')

#conexion = Conector()
#print(conexion.listar())

