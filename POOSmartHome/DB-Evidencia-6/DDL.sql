-- Crear y usar la base de datos
DROP DATABASE IF EXISTS poosmarthome;
CREATE DATABASE poosmarthome;
USE poosmarthome;

-- TABLA: usuarios
-- Almacena información de los usuarios del sistema

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(20) NOT NULL DEFAULT 'standard',
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- TABLA: dispositivos
-- Almacena los dispositivos inteligentes del hogar

CREATE TABLE dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    esencial BOOLEAN NOT NULL DEFAULT TRUE
    
);


-- TABLA: automatizaciones
-- Almacena las automatizaciones configuradas
-- Relación: Una automatización pertenece a un dispositivo

CREATE TABLE automatizaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_dispositivo INT NOT NULL,
    activa BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

CREATE TABLE registro_actividad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(100),
    accion VARCHAR(255) NOT NULL,
    detalle TEXT
);