
/* CREATE DATABASE IF NOT EXISTS `prueba` ;
USE `prueba` ;
*/

CREATE TABLE venta (
codigo INT(8) NOT NULL PRIMARY KEY,
fecha DATE NOT NULL,
precioTotal  DOUBLE(10,2) NOT NULL,
idProducto INT(8) NOT NULL,
idCliente INT(8),
FOREIGN KEY(idProducto) REFERENCES producto(id),
FOREIGN KEY(idCliente) REFERENCES cliente(dni));

/*
ALTER TABLE venta
MODIFY fecha VARCHAR (255);
SET SQL_SAFE_UPDATES = 0;
UPDATE venta
SET fecha = date_format(fecha,"%b/%d/%Y");
*/

/*
ALTER TABLE ventas ADD FOREIGN KEY(idProducto) REFERENCES producto(id);
ALTER TABLE ventas ADD FOREIGN KEY(idCliente) REFERENCES clientes(dni);
*/

INSERT INTO venta (codigo, fecha, precioTotal, id_producto, id_cliente)
VALUES
  (1,'2024-03-11', 23501.03, 21, 12345678),
  (2,'2024-04-19', 297950.62, 1, 11223344),
  (3,'2024-05-02', 34129.99, 4, 87654321);

CREATE TABLE cliente (
dni INT(8) NOT NULL PRIMARY KEY,
nombre VARCHAR(32) NOT NULL,
apellido  VARCHAR(32) NOT NULL,
contacto VARCHAR(15)
);

INSERT INTO cliente (dni, nombre, apellido, contacto)
VALUES
  (12345678,'Jorge', 'Gómez', '1146054003'),
  (11223344,'Florencia', 'Bonino', '1136027799'),
  (87654321,'Albano', 'Rodríguez', '1144662200');

CREATE TABLE producto (
  id INT(8) NOT NULL PRIMARY KEY,
  nombre VARCHAR(32) NOT NULL,
  marca VARCHAR(20) NOT NULL,
  descripcion VARCHAR(50) NOT NULL,
  precio DOUBLE(10,2) NOT NULL,
  cantidad INT(4) NOT NULL
);

INSERT INTO producto (id, nombre, marca, descripcion, precio, cantidad)
VALUES
  (1,'EOS R6 Mark II', 'CANON', 'Cámara mirrorless con kit RF 24-105mm', 297950.62, 4),
  (2,'A6100', 'SONY', 'Cámara mirrorless Alpha A6100 con kit Sony E PZ 16-50mm', 1650000, 1),
  (3,'ILCE-7M4K', 'SONY', 'Cámara mirrorless Alpha con Kit A7 IV OSS', 3199999.99, 2),
  (4,'D7500', 'NIKON', 'Cámara mirrorless con kit Nikkor AF-S DX 18-140mm', 2180500, 5);


SELECT * FROM ventas;

