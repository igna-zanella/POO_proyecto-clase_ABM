-- -----------------------------------------------------
-- Database Prueba
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `prueba` ;
USE `prueba` ;



create table direccion(
id int(11) not null,
calle varchar(32),
numero int(11) not null ,
codigoP int(11) not null);



alter table direccion add primary key (id);
CREATE TABLE educacion (
  id_educacion INT PRIMARY KEY,
  educacionMax VARCHAR(30) NOT NULL,
  institucion VARCHAR(80) NOT NULL,
  titulo VARCHAR(30) NOT NULL
  
);

INSERT INTO educacion (id_educacion, educacionMax, institucion, titulo)
VALUES
  (100,'Universitario', 'Universidad Nacional de La Plata', 'Licenciado '),
  (101,'Ingeniería', 'Universidad de Buenos Aires', 'Ingeniería de Software'),
  (102,'Terciario', 'Educacion Buenos Aires', 'Programador');


create table usuario (
dni int(8) not null primary key,
nombre varchar(20) not null,
apellido  varchar(20) not null,
direccion int(5),
educacion int(5),
foreign key(direccion) references direccion(id));


alter table usuario add foreign key(direccion) references direccion(id);
alter table usuario add foreign key(educacion) references educacion(id_educacion);

INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('1', 'Lavalle', '421', '5700');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('2', 'Ituzaingo', '280', '5700');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('3', 'Cordoba', '500', '8600');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('4', 'Tucuman', '600', '8700');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('5', 'jujuy', '700', '5421');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('6', 'Libertad', '250', '3200');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('7', 'Salta', '325', '5600');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('8', 'Uriarte', '5201', '4587');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('9', 'Misiones', '3265', '5600'); 
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('10', 'Chubut', '845', '7500');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('11', 'Neuquen', '369', '8500');
INSERT INTO `prueba`.`direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES ('12', 'Mendoza', '2569', '8900');
INSERT INTO `prueba`.`usuario` (`dni`, `nombre`, `apellido`, `direccion`, educacion) VALUES ('11222333', 'Ana', 'Gomez', 1,100);
INSERT INTO `prueba`.`usuario` (`dni`, `nombre`, `apellido`, `direccion`, educacion) VALUES ('22333444', 'Maria', 'Sanchez', 2,101);
INSERT INTO `prueba`.`usuario` (`dni`, `nombre`, `apellido`, `direccion`, educacion) VALUES ('33444555', 'Daniel', 'Terrible', 3,100);
INSERT INTO `prueba`.`usuario` (`dni`, `nombre`, `apellido`, `direccion`, educacion) VALUES ('33222111', 'Rafael', 'Nadal', 1,102);
select * from direccion;

