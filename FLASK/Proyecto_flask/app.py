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
    cur.execute('select * from usuario')
    datos = cur.fetchall()
    # print(datos)
    return render_template('listar.html', datos = datos)

@app.route('/agregar', methods=['POST','GET'])
def agregar():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('select * from direccion')
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
        cur.execute('delete from usuario where dni = {0}'.format(dni))
        cur.connection.commit()
        return redirect(url_for('listar'))

@app.route('/obtener/<id>')
def obtener(id):
        cur = mysql.connection.cursor()
        # cur.execute('select * from usuario where dni = %s' % (id))
        cur.execute('select usuario.dni, usuario.nombre, usuario.apellido, usuario.direccion, usuario.educacion, direccion.id, direccion.calle, direccion.numero, direccion.codigoP from usuario, direccion where dni = %s' % (id))
        usuario = cur.fetchall()
        return render_template('editar.html', usuario = usuario[0], dire = usuario)

@app.route('/actualizar/<dni>', methods=['POST'])
def actualizar(dni):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        educacion = request.form['educacion']
        
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE usuario set nombre = %s, 
                    apellido = %s, 
                    direccion = %s, 
                    educacion = %s where dni = %s''', (nombre, apellido, direccion, educacion, dni))
        cur.connection.commit()
        return  redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(port=3000,debug=True)
