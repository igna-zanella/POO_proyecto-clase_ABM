-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-05-2024 a las 16:23:38
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

CREATE TABLE `direccion` (
  `id` int(11) NOT NULL,
  `calle` varchar(32) DEFAULT NULL,
  `numero` int(11) NOT NULL,
  `codigoP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `direccion`
--

INSERT INTO `direccion` (`id`, `calle`, `numero`, `codigoP`) VALUES
(1, 'Lavalle', 421, 5700),
(2, 'Ituzaingo', 280, 5700),
(3, 'Cordoba', 500, 8600),
(4, 'Tucuman', 600, 8700),
(5, 'jujuy', 700, 5421),
(6, 'Libertad', 250, 3200),
(7, 'Salta', 325, 5600),
(8, 'Uriarte', 5201, 4587),
(9, 'Misiones', 3265, 5600),
(10, 'Chubut', 845, 7500),
(11, 'Neuquen', 369, 8500),
(12, 'Mendoza', 2569, 8900);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `educacion`
--

CREATE TABLE `educacion` (
  `id_educacion` int(11) NOT NULL,
  `educacionMax` varchar(30) NOT NULL,
  `institucion` varchar(80) NOT NULL,
  `titulo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `educacion`
--

INSERT INTO `educacion` (`id_educacion`, `educacionMax`, `institucion`, `titulo`) VALUES
(100, 'Universitario', 'Universidad Nacional de La Plata', 'Licenciado '),
(101, 'Ingeniería', 'Universidad de Buenos Aires', 'Ingeniería de Software'),
(102, 'Terciario', 'Educacion Buenos Aires', 'Programador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `dni` int(8) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `direccion` int(5) DEFAULT NULL,
  `educacion` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`dni`, `nombre`, `apellido`, `direccion`, `educacion`) VALUES
(11222333, 'Ana', 'Gomez', 1, 100),
(22333444, 'Maria', 'Sanchez', 2, 101),
(33222111, 'Rafael', 'Nadal', 1, 102),
(33444555, 'Daniel', 'Terrible', 3, 100);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `direccion`
--
ALTER TABLE `direccion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `educacion`
--
ALTER TABLE `educacion`
  ADD PRIMARY KEY (`id_educacion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`dni`),
  ADD KEY `direccion` (`direccion`),
  ADD KEY `educacion` (`educacion`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`direccion`) REFERENCES `direccion` (`id`),
  ADD CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`direccion`) REFERENCES `direccion` (`id`),
  ADD CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`educacion`) REFERENCES `educacion` (`id_educacion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
