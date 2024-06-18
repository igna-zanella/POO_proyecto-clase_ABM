-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-06-2024 a las 02:41:58
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `dni` int(8) NOT NULL,
  `nombre` varchar(32) NOT NULL,
  `apellido` varchar(32) NOT NULL,
  `contacto` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`dni`, `nombre`, `apellido`, `contacto`) VALUES
(11223344, 'Florencia', 'Bonino', '1136027799'),
(12345678, 'Jorge', 'Gómez', '1146054003'),
(21312300, 'Ana', 'Rezza', '1132524085'),
(22331122, 'Carlos', 'González', '1154237784'),
(33222211, 'Lolo', 'Lopez', '1132352412'),
(87654321, 'Albano', 'Rodríguez', '1144662200');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(8) NOT NULL,
  `nombre` varchar(32) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `precio` double(10,2) NOT NULL,
  `cantidad` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `marca`, `descripcion`, `precio`, `cantidad`) VALUES
(1, 'EOS R6 Mark II', 'CANON', 'Cámara mirrorless con kit RF 24-105mm. ', 4590000.00, 4),
(2, 'A6100', 'SONY', 'Cámara mirrorless Alpha A6100 con kit Sony E PZ 16', 1650000.00, 1),
(3, 'ILCE-7M4K', 'SONY', 'Cámara mirrorless Alpha con Kit A7 IV OSS', 3199999.99, 2),
(4, 'D7500', 'NIKON', 'Cámara mirrorless con kit Nikkor AF-S DX 18-140mm', 2180500.00, 5),
(5, 'Z7', 'NIKON', 'Formato FX 14 CPS Disparos Continuos', 3037000.00, 2),
(6, 'Zfc', 'NIKON', 'Formato DX 20.9 Megapíxeles 11 CPS', 1039000.00, 4),
(8, 'EOS Rebel6', 'CANON', 'Mirrorless. PROCESADOR DE IMÁGENES DIGIC X.', 2520000.00, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `codigo` int(8) NOT NULL,
  `fecha` varchar(255) DEFAULT NULL,
  `precioTotal` double(10,2) NOT NULL,
  `idProducto` int(8) NOT NULL,
  `idCliente` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`codigo`, `fecha`, `precioTotal`, `idProducto`, `idCliente`) VALUES
(1, '2024-03-12', 0.00, 1, 12345678),
(2, '2024-03-23', 0.00, 5, 11223344),
(3, '2024-04-04', 0.00, 8, 21312300),
(4, '2024-04-11', 0.00, 2, 22331122),
(5, '2024-04-26', 0.00, 3, 87654321),
(20, '2024-06-03', 0.00, 1, 33222211);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`dni`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `idProducto` (`idProducto`),
  ADD KEY `idCliente` (`idCliente`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`id`),
  ADD CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`dni`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
