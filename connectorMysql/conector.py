
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
                database = 'prueba_02-05'
            )
        except Error as res:
            print(f'No se pudo establecer la conexión: {res}')

    def listar(self):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                cur.execute('select usuario.nombre, usuario.apellido, usuario.dni, direccion.calle, direccion.numero, direccion.codigoP, educacion.educacionMax, educacion.titulo  from usuario, direccion, educacion where usuario.direccion = direccion.id and usuario.educacion = educacion.id_educacion')
                respuesta = cur.fetchall()
                return respuesta
            except Error as res:
                print(f'No se pudo listar: {res}')
                
    def registro(self, usuario):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                sql = (''' insert into usuario
                        (dni, nombre, apellido, direccion, educacion)
                        value ({0}, '{1}', '{2}', {3}, {4})
                    ''')
                cur.execute(sql.format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                self.conexion.commit()
                print('Agregado')
            except Error as res:
                print(f'No se pudo agregar al registro: {res}')
                
    def actualizar(self, usuario):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                sql = (''' update usuario 
                        set
                        nombre ='{0}',
                        apellido = '{1}', 
                        direccion = {2},
                        educacion = {3}
                        where dni = {4}
                    ''')
                cur.execute(sql.format(usuario[1], usuario[2], usuario[3], usuario[4], usuario[0]))
                self.conexion.commit()
                print('Actualizado')
            except Error as res:
                print(f'No se pudo agregar al registro: {res}')

    def eliminar(self, usuario):
        if self.conexion.is_connected():
            try:
                cur = self.conexion.cursor()
                sql = (''' delete from usuario where dni = {0}
                    ''')
                cur.execute(sql.format(usuario))
                self.conexion.commit()
                print('Eliminado')
            except Error as res:
                print(f'No se pudo eliminar al usuario: {res}')





#conexion = Conector()
#print(conexion.listar())

