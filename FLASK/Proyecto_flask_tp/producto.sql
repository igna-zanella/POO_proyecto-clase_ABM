-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2024 a las 02:46:04
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
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(8) NOT NULL,
  `nombre` varchar(32) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `descripcion` varchar(400) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `cantidad` int(4) DEFAULT 0,
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
(30, 'TUG', 'BLACKMAGIC', 'SN', 800.00, 1, 'nodisponible.png'),
(32, 'qa12', 'RED', 'Cine ultra', 10000.00, 0, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
