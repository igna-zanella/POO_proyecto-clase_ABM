
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime

now = datetime.now()



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'v02'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

# ------------------------ VENTAS (HOME) -----------------------------------

@app.route('/')
def listar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT venta.codigo, venta.fecha, venta.precioTotal, venta.idProducto, venta.idCliente, producto.id, producto.nombre, producto.marca, producto.descripcion, producto.precio, producto.cantidad, cliente.dni, cliente.nombre, cliente.apellido, cliente.contacto FROM venta, producto, cliente WHERE venta.idProducto = producto.id AND venta.idCliente = cliente.dni ORDER BY venta.fecha')
    datos = cur.fetchall()
    # flash("Listado de Operaciones")
    #app.secret_key = 'mysecretkey'
    return render_template('listar.html', datos = datos)
#venta.codigo[0], venta.fecha[1], venta.precioTotal[2], venta.idProducto[3], venta.idCliente[4], producto.id[5], producto.nombre[6], producto.marca[7], producto.descripcion[8], producto.precio[9], producto.cantidad[10], cliente.dni[11], cliente.nombre[12], cliente.apellido[13], cliente.contacto[14]

@app.route('/agregar', methods=['POST','GET'])
def agregar():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM producto ORDER BY marca')
        productos = cur.fetchall()
        
        curCli = mysql.connection.cursor()
        curCli.execute('SELECT * FROM cliente ORDER BY apellido')
        clientes = curCli.fetchall()

        
        return render_template('agregar.html', producto = productos, cliente = clientes)
    elif request.method == 'POST':
        codigo = request.form['codigo']
        # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')['fecha']
        fecha = request.form['fecha']
        # precioTotal = request.form['precioTotal']
        idProducto = request.form['idProducto']
        idCliente = request.form['idCliente']
        
        # cur = mysql.connection.cursor()
        # cur.execute('INSERT INTO venta, producto (codigo.venta, fecha.venta, idProducto.venta, idCliente.venta, sum(cantidad.producto - 1)) VALUES (%s, %s, %s, %s, %s)', (codigo, fecha, idProducto, idCliente, cantidad))
        # cur.connection.commit()
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO venta (codigo, fecha, idProducto, idCliente) VALUES (%s, %s, %s, %s)', (codigo, fecha, idProducto, idCliente))
        cur.connection.commit()
        
        curCant = mysql.connection.cursor()
        # curCant.execute('SELECT SUM(cantidad-1) AS stock FROM producto WHERE id=1 VALUES (%s)', (stock))
        # curCant.execute('SELECT SUM(cantidad-1) AS stock FROM producto WHERE id like "A1%" ')
        curCant.execute('SELECT * FROM producto,venta; UPDATE producto SET cantidad = cantidad + 1 WHERE id = idProducto')
        curCant.connection.commit()
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
    curp.execute('SELECT * FROM producto ORDER BY marca')
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
        img = request.form['img']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO producto (id, nombre, marca, descripcion, precio, cantidad, img) VALUES (%s, %s, %s, %s, %s, %s, %s)', (id, nombre, marca, descripcion, precio, cantidad, img))
        cur.connection.commit()
        return redirect(url_for('listarProducto'))
    
@app.route('/eliminarProducto/<string:id>')
def eliminarProducto(id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM producto WHERE id = {0}'.format(id))
        cur.connection.commit()
        return redirect(url_for('listarProducto'))

@app.route('/buscarProducto', methods=['GET','POST'])
def buscarProducto():
    if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM producto')
            productos = cur.fetchall()

            return render_template('buscarProducto.html', productos = productos)
    elif request.method == 'POST':
        marca = request.form['marca']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM producto WHERE marca LIKE "%%%s%%"' % (marca))
        productos = cur.fetchall()
        if productos:
            flash("Resultados de la búsqueda")
        else:
            flash("No hay resultados para su búsqueda")
        return render_template('listarProducto.html', productos = productos)
    

@app.route('/obtenerProducto/<id>')
def obtenerProducto(id):
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM producto WHERE id = %s' % (id))
        producto = cur.fetchall()
        
        return render_template('editarProducto.html', productos = producto[0])

@app.route('/actualizarProducto/<id>', methods=['POST', 'GET'])
def actualizarProducto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        
        if(request.form['img']):
            img = request.form['img']
            
            cur = mysql.connection.cursor()
            cur.execute('''UPDATE producto SET nombre = %s, 
                        marca = %s, 
                        descripcion = %s, 
                        precio = %s,
                        cantidad = %s,
                        img = %s WHERE id = %s''', (nombre, marca, descripcion, precio, cantidad, img, id))
            cur.connection.commit()
        else:
            img  ='nodisponible.png'
            cur = mysql.connection.cursor()
            cur.execute('''UPDATE producto SET nombre = %s, 
                        marca = %s, 
                        descripcion = %s, 
                        precio = %s,
                        cantidad = %s,
                        img = %s WHERE id = %s''', (nombre, marca, descripcion, precio, cantidad, img, id))
            cur.connection.commit()

        return  redirect(url_for('listarProducto'))



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

@app.route('/buscarCliente', methods=['GET','POST'])
def buscarCliente():
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
            cur.execute('SELECT * FROM cliente')
            clientes = cur.fetchall()

            return render_template('buscar.html', clientes = clientes)
    elif request.method == 'POST':
        apellido = request.form['apellido']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cliente WHERE apellido LIKE "%%%s%%"' % (apellido))
        clientes = cur.fetchall()
        if clientes:
            flash("Resultados de la búsqueda")
        else:
            flash("No hay resultados para su búsqueda")
        return render_template('listarCliente.html', clientes = clientes)

@app.route('/obtenerCliente/<dni>')
def obtenerCliente(dni):
        curCliente= mysql.connection.cursor()
        curCliente.execute('SELECT * FROM cliente WHERE dni = %s' % (dni))
        cliente = curCliente.fetchall()
        
        return render_template('editarCliente.html', clientes = cliente[0])

@app.route('/actualizarCliente/<dni>', methods=['POST'])
def actualizarCliente(dni):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contacto = request.form['contacto']
        
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE cliente SET nombre = %s, 
                    apellido = %s, 
                    contacto = %s WHERE dni = %s''', (nombre, apellido, contacto, dni))
        cur.connection.commit()

        return  redirect(url_for('listarCliente'))
    
# ------------------------ FIN CLIENTE -------------------------------------


@app.route('/obtener/<id>')
def obtener(id):
        curProducto= mysql.connection.cursor()
        curProducto.execute('SELECT * FROM producto')
        producto = curProducto.fetchall()
        
        curCliente= mysql.connection.cursor()
        curCliente.execute('SELECT * FROM cliente')
        cliente = curCliente.fetchall()
        
        cur = mysql.connection.cursor()
        # cur.execute('SELECT * FROM usuario WHERE dni = %s' % (id))
        cur.execute('SELECT * FROM venta, producto direccion WHERE codigo = %s' % (id))
        venta = cur.fetchall()

        # usuario.dni[0], usuario.nombre[1], usuario.apellido[2], usuario.direccion[3], usuario.educacion[4], direccion.id[5], direccion.calle[6], direccion.numero[7], direccion.codigoP[8] 
        
        return render_template('editar.html', ventahtml = venta[0], clientes = cliente, productos = producto, venCli = venta, venProd = producto)

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
    
    if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute('SELECT venta.codigo, venta.fecha, venta.precioTotal, venta.idProducto, venta.idCliente, producto.id, producto.nombre, producto.marca, producto.descripcion, producto.precio, producto.cantidad, cliente.dni, cliente.nombre, cliente.apellido, cliente.contacto FROM venta, producto, cliente WHERE venta.idProducto = producto.id AND venta.idCliente = cliente.dni ORDER BY venta.fecha')
            datos = cur.fetchall()
            #venta.codigo[0], venta.fecha[1], venta.precioTotal[2], venta.idProducto[3], venta.idCliente[4], producto.id[5], producto.nombre[6], producto.marca[7], producto.descripcion[8], producto.precio[9], producto.cantidad[10], cliente.dni[11], cliente.nombre[12], cliente.apellido[13], cliente.contacto[14]

            return render_template('buscar.html', datos = datos)
    elif request.method == 'POST':
        apellido = request.form['apellido']
        
        cur = mysql.connection.cursor()
        cur.execute('SELECT venta.codigo, venta.fecha, venta.precioTotal, venta.idProducto, venta.idCliente, producto.id, producto.nombre, producto.marca, producto.descripcion, producto.precio, producto.cantidad, cliente.dni, cliente.nombre, cliente.apellido, cliente.contacto FROM venta, producto, cliente WHERE  apellido LIKE "%%%s%%"' % (apellido))
        datos = cur.fetchall()
        
        curCli = mysql.connection.cursor()
        curCli.execute('SELECT * FROM cliente WHERE apellido LIKE "%%%s%%"' % (apellido))
        clientes = curCli.fetchall()
        if datos:
            flash("Resultados de la búsqueda")
        else:
            flash("No hay resultados para su búsqueda")
        return render_template('listarBusqueda.html', datos = datos, clientes = clientes)


if __name__ == '__main__':
    app.run(port=3000,debug=True)
