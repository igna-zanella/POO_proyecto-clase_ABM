from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_db'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def listar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT usuario.dni, usuario.nombre, usuario.apellido, usuario.direccion, usuario.educacion, direccion.calle, direccion.numero, educacion.educacionMax FROM usuario, direccion, educacion WHERE usuario.direccion = direccion.id AND usuario.educacion = educacion.id_educacion ORDER BY apellido')
    datos = cur.fetchall()
    flash("Listado de Usuarios")
    #app.secret_key = 'mysecretkey'
    return render_template('listar.html', datos = datos)

@app.route('/agregar', methods=['POST','GET'])
def agregar():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM direccion')
        datos = cur.fetchall()
        
        curEdu = mysql.connection.cursor()
        curEdu.execute('SELECT * FROM educacion')
        educacion = curEdu.fetchall()
        
        return render_template('agregar.html', direccion= datos, educacionHtml = educacion)
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
        curEducacion.execute('SELECT usuario.dni, usuario.educacion, educacion.id_educacion, educacion.educacionMax, educacion.titulo FROM usuario, educacion WHERE dni = %s' % (id))
        educacion= curEducacion.fetchall()
        
        curDireccion= mysql.connection.cursor()
        # cuDireccion.execute('SELECT * FROM direccion')
        curDireccion.execute('SELECT * FROM direccion')
        direccion= curDireccion.fetchall()
        
        cur = mysql.connection.cursor()
        # cur.execute('SELECT * FROM usuario WHERE dni = %s' % (id))
        cur.execute('SELECT * FROM usuario, direccion WHERE dni = %s' % (id))
        usuario = cur.fetchall()

        # usuario.dni[0], usuario.nombre[1], usuario.apellido[2], usuario.direccion[3], usuario.educacion[4], direccion.id[5], direccion.calle[6], direccion.numero[7], direccion.codigoP[8] 
        
        return render_template('editar.html', usuariohtml = usuario[0], dire = direccion, edu = educacion, usuDire = usuario, usuEdu = educacion)

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

@app.route('/buscar', methods=['GET','POST'])
def buscar():
    # nombre = request.form['nombre']
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM usuario WHERE nombre LIKE "%%%s%%"' % (nombre))
    # datos = cur.fetchall()
    # if datos:
    #      flash("Resultados de la búsqueda")
    # else:
    #      flash("No hay resultados para su búsqueda")
    # return render_template('listar.html', datos = datos)

    if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM usuario')
            datos = cur.fetchall()

            return render_template('buscar.html', datos= datos)
    elif request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE nombre LIKE "%%%s%%" ORDER BY apellido' % (nombre))
        datos = cur.fetchall()
        if datos:
            flash("Resultados de la búsqueda")
        else:
            flash("No hay resultados para su búsqueda")
        return render_template('listar.html', datos = datos)

if __name__ == '__main__':
    app.run(port=3000,debug=True)
