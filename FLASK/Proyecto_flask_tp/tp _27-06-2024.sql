-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2024 a las 02:06:12
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
-- Base de datos: `v02`
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
(11223344, 'Florencia', 'Bonino', '1136027790'),
(12345678, 'Jorge', 'Gómez', '1146054003'),
(21312300, 'Ana', 'Rezza', '1132524085'),
(22331122, 'Carlos', 'González', '1154237784'),
(33222211, 'Facundo', 'Lopez', '1132352412'),
(87654321, 'Albano', 'Rodríguez', '1144662200');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(8) NOT NULL,
  `nombre` varchar(32) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `descripcion` varchar(400) NOT NULL,
  `precio` double(10,2) NOT NULL,
  `cantidad` int(4) NOT NULL,
  `img` varchar(60) DEFAULT 'nodisponible.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `marca`, `descripcion`, `precio`, `cantidad`, `img`) VALUES
(1, 'EOS R6 Mark II', 'CANON', 'Cámara mirrorless con kit RF 24-105mm. ', 2400.00, 4, '1.png'),
(2, 'A6100', 'SONY', 'Cámara mirrorless Alpha A6100 con kit Sony E PZ 16', 748.00, 1, '2.png'),
(3, 'ILCE-7M4K', 'SONY', 'Cámara mirrorless Alpha con Kit A7 IV OSS', 2799.00, 2, '3.png'),
(4, 'D7500', 'NIKON', 'Cámara mirrorless con kit Nikkor AF-S DX 18-140mm', 1200.00, 5, '4.png'),
(5, 'Z7', 'NIKON', 'Formato FX 14 CPS Disparos Continuos', 2275.00, 3, '5.png'),
(6, 'ZFC', 'NIKON', 'Formato DX 20.9 Megapíxeles 11 CPS ', 895.00, 5, '6.png'),
(8, 'EOS 6D Mark II', 'CANON', 'Mirrorless. PROCESADOR DE IMÁGENES DIGIC X.', 1450.00, 0, '8.png'),
(16, 'EOS 5D', 'CANON', 'Fullframe', 604.00, 1, 'nodisponible.png'),
(18, 'D3500', 'NIKON', 'Video en 1080p', 320.00, 1, 'nodisponible.png'),
(30, 'TUG', 'BLACKMAGIC', 'SN', 800.00, 1, 'nodisponible.png');

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
