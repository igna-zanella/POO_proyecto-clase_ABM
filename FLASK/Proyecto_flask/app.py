from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_db'
mysql = MySQL(app)
@app.route('/')
def listar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario ORDER BY apellido')
    datos = cur.fetchall()
    # print(datos)
    return render_template('listar.html', datos = datos)

@app.route('/agregar', methods=['POST','GET'])
def agregar():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM direccion')
        datos = cur.fetchall()
        return render_template('agregar.html', direccion= datos)
    elif request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        educacion = request.form['educacion']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (dni, nombre, apellido, direccion, educacion) VALUES (%s, %s, %s, %s, %s)', (dni, nombre, apellido, direccion, educacion))
        cur.connection.commit()
        return  redirect(url_for('listar'))

@app.route('/eliminar/<string:dni>')
def eliminar(dni):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM usuario WHERE dni = {0}'.format(dni))
        cur.connection.commit()
        return redirect(url_for('listar'))

@app.route('/obtener/<id>')
def obtener(id):
        curEducacion= mysql.connection.cursor()
        # curEducacion.execute('SELECT * FROM direccion')
        curEducacion.execute('SELECT educacion.id_educacion, educacion.educacionMax, educacion.institucion, educacion.titulo FROM educacion')
        educacion= curEducacion.fetchall()
        
        cur = mysql.connection.cursor()
        # cur.execute('SELECT * FROM usuario WHERE dni = %s' % (id))
        cur.execute('SELECT usuario.dni, usuario.nombre, usuario.apellido, usuario.direccion, usuario.educacion, direccion.id, direccion.calle, direccion.numero, direccion.codigoP FROM usuario, direccion WHERE dni = %s' % (id))
        usuario = cur.fetchall()
        
        return render_template('editar.html', usuariohtml = usuario[0], dire = usuario, edu = educacion)

@app.route('/actualizar/<dni>', methods=['POST'])
def actualizar(dni):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        educacion = request.form['educacion']
        
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE usuario SET nombre = %s, 
                    apellido = %s, 
                    direccion = %s, 
                    educacion = %s WHERE dni = %s''', (nombre, apellido, direccion, educacion, dni))
        cur.connection.commit()

        return  redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(port=3000,debug=True)
