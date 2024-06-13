
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime

now = datetime.now()



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tp'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

# ------------------------ VENTAS (HOME) -----------------------------------

@app.route('/')
def listar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT venta.codigo, venta.fecha, venta.precioTotal, venta.idProducto, venta.idCliente, producto.id, producto.nombre, producto.marca, producto.descripcion, producto.precio, producto.cantidad, cliente.dni, cliente.nombre, cliente.apellido, cliente.contacto FROM venta, producto, cliente WHERE venta.idProducto = producto.id AND venta.idCliente = cliente.dni')
    datos = cur.fetchall()
    # flash("Listado de Operaciones")
    #app.secret_key = 'mysecretkey'
    return render_template('listar.html', datos = datos)
#venta.codigo[0], venta.fecha[1], venta.precioTotal[2], venta.idProducto[3], venta.idCliente[4], producto.id[5], producto.nombre[6], producto.marca[7], producto.descripcion[8], producto.precio[9], producto.cantidad[10], cliente.dni[11], cliente.nombre[12], cliente.apellido[13], cliente.contacto[14]

@app.route('/agregar', methods=['POST','GET'])
def agregar():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM producto')
        productos = cur.fetchall()
        
        curCli = mysql.connection.cursor()
        curCli.execute('SELECT * FROM cliente')
        clientes = curCli.fetchall()

        
        return render_template('agregar.html', producto = productos, cliente = clientes)
    elif request.method == 'POST':
        codigo = request.form['codigo']
        # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')['fecha']
        fecha = request.form['fecha']
        precioTotal = request.form['precioTotal']
        idProducto = request.form['idProducto']
        idCliente = request.form['idCliente']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO venta (codigo, fecha, precioTotal, idProducto, idCliente) VALUES (%s, %s, %s, %s, %s)', (codigo, formatted_date, precioTotal, idProducto, idCliente))
        cur.connection.commit()
        return  redirect(url_for('listar'))
    

@app.route('/eliminar/<string:codigo>')
def eliminar(codigo):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM venta WHERE codigo = {0}'.format(codigo))
        cur.connection.commit()
        return redirect(url_for('listar'))

# ------------------------ FIN VENTAS --------------------------------------
# ------------------------ PRODUCTOS ---------------------------------------

@app.route('/listarProducto')
def listarProducto():
    curp = mysql.connection.cursor()
    curp.execute('SELECT * FROM producto ORDER BY id')
    productos = curp.fetchall()
    # flash("Listado de Usuarios")
    #app.secret_key = 'mysecretkey'
    return render_template('listarProducto.html', productos = productos)

@app.route('/agregarProducto', methods=['POST','GET'])
def agregarProducto():
    if request.method == 'GET':
        curp = mysql.connection.cursor()
        curp.execute('SELECT * FROM producto')
        productos = curp.fetchall()
        return render_template('agregarProducto.html', productos = productos,  title = "Agregar Producto")

    elif request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        marca = request.form['marca']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO producto (id, nombre, marca, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s, %s, %s)', (id, nombre, marca, descripcion, precio, cantidad))
        cur.connection.commit()
        return redirect(url_for('listarProducto'))
    
@app.route('/eliminarProducto/<string:id>')
def eliminarProducto(id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM producto WHERE id = {0}'.format(id))
        cur.connection.commit()
        return redirect(url_for('listarProducto'))

# ------------------------ FIN PRODUCTOS -----------------------------------
# ------------------------ CLIENTE -----------------------------------------

@app.route('/listarCliente')
def listarCliente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente ORDER BY apellido')
    clientes = cur.fetchall()
    # flash("Listado de Usuarios")
    #app.secret_key = 'mysecretkey'
    return render_template('listarCliente.html', clientes = clientes)

@app.route('/agregarCliente', methods=['POST','GET'])
def agregarCliente():
    if request.method == 'GET':
        curc = mysql.connection.cursor()
        curc.execute('SELECT * FROM cliente')
        clientes = curc.fetchall()
                
        return render_template('agregarCliente.html', clientes = clientes)
    elif request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = request.form['contacto']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO cliente (dni, nombre, apellido, contacto) VALUES (%s, %s, %s, %s)', (dni, nombre, apellido, contacto))
        cur.connection.commit()
        return redirect(url_for('listarCliente'))
    
    
@app.route('/eliminarCliente/<string:dni>')
def eliminarCliente(dni):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM cliente WHERE dni = {0}'.format(dni))
        cur.connection.commit()
        return redirect(url_for('listarCliente'))
    
# ------------------------ FIN CLIENTE -------------------------------------


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
        
        return render_template('editar.html', usuariohtml = usuario[0], dire = direccion, Cli = educacion, usuDire = usuario, usuEdu = educacion)

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
