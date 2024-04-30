
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
                database = 'p2304'
            )
        except Error as res:
            print(f'No se pudo establecer la conexión: {res}')

    def listar(self):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                #cur.execute('select * from usuario')
                cur.execute('select usuario.nombre, usuario.apellido, usuario.dni, direccion.calle, direccion.numero, direccion.codigoP from usuario, direccion where usuario.direccion = direccion.id')
                respuesta = cur.fetchall()
                return respuesta
            except Error as res:
                print(f'No se pudo listar: {res}')
                
    def registro(self, usuario):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                sql = (''' insert into usuario
                        (dni, nombre, apellido, direccion)
                        value ({0}, '{1}', '{2}', {3})
                    ''')
                cur.execute(sql.format(usuario[0], usuario[1], usuario[2], usuario[3]))
                self.conexion.commit()
                print('Agregado')
            except Error as res:
                print(f'No se pudo agregar al registro: {res}')
                
    def actualizar(self, usuario):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                sql = (''' update usuario set
                        (nombre, apellido)
                        value ('{1}', '{2}')
                    ''')
                cur.execute(sql.format(usuario[1], usuario[2]))
                self.conexion.commit()
                print('Actualizado')
            except Error as res:
                print(f'No se pudo agregar al registro: {res}')

#conexion = Conector()
#print(conexion.listar())

