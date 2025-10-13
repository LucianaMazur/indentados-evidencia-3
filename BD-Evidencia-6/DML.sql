-- -----------------
-- TABLAS
-- -----------------

CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    mail VARCHAR(50),
    contraseña VARCHAR(50),
    rol VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Dispositivos (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    tipo VARCHAR(30),
    estado VARCHAR(20),
    es_esencial BOOLEAN
);

CREATE TABLE IF NOT EXISTS Automatizaciones (
    id_automatizacion INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS Registro_Actividad (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    fecha_hora DATETIME,
    accion VARCHAR(50),
    id_usuario INT,
    id_dispositivo INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);

CREATE TABLE IF NOT EXISTS Usuario_Dispositivo (
    id_usuario INT,
    id_dispositivo INT,
    fecha_asignacion DATETIME,
    PRIMARY KEY (id_usuario, id_dispositivo),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);

CREATE TABLE IF NOT EXISTS Dispositivo_Automatizacion (
    id_dispositivo INT,
    id_automatizacion INT,
    fecha_configuracion DATETIME,
    PRIMARY KEY (id_dispositivo, id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES Automatizacion(id_automatizacion)
);

-- -----------------
-- INSERTS
-- -----------------

-- Usuario
INSERT INTO Usuarios (username, password, nombre, email, role, activo) VALUES
('juanp', 'contr123', 'Juan Pérez', 'juan.perez@email.com', 'admin', 1),
('mariag', 'contr456', 'María González', 'maria.gonzalez@email.com', 'estandar', 1),
('carlosl', 'contr789', 'Carlos López', 'carlos.lopez@email.com', 'estandar', 1),
('anam', 'contr101', 'Ana Martínez', 'ana.martinez@email.com', 'estandar', 1),
('luisr', 'contr202', 'Luis Rodríguez', 'luis.rodriguez@email.com', 'estandar', 1),
('elenas', 'contr303', 'Elena Sánchez', 'elena.sanchez@email.com', 'admin', 1),
('pedror', 'contr404', 'Pedro Romero', 'pedro.romero@email.com', 'estandar', 1),
('sofiat', 'contr505', 'Sofía Torres', 'sofia.torres@email.com', 'admin', 1),
('miguelh', 'contr606', 'Miguel Herrera', 'miguel.herrera@email.com', 'estandar', 1),
('lauraj', 'contr707', 'Laura Jiménez', 'laura.jimenez@email.com', 'estandar', 1);


-- Dispositivo
INSERT INTO Dispositivos (nombre, tipo) VALUES
('Cafetera Inteligente', 'electrodoméstico'),
('Televisor Sala', 'entretenimiento'),
('Consola Juegos', 'entretenimiento'),
('Luz Dormitorio', 'iluminación'),
('Luz Cocina', 'iluminación'),
('Cerradura Inteligente', 'seguridad'),
('Sensor Movimiento', 'seguridad'),
('Cámara Entrada', 'seguridad'),
('Router WiFi', 'conectividad'),
('Televisor Pieza', 'entretenimiento');

-- Automatizacion
INSERT INTO Automatizaciones (nombre, id_dispositivo, activa) VALUES
('modo ahorro', 6, 1),
('control parental', 3, 2),
('programar cafetera', 1, 3);


-- Dispositivo_Automatizacion
INSERT INTO Dispositivo_Automatizacion (id_dispositivo, id_automatizacion, fecha_configuracion) VALUES
(1, 3, '2025-08-22 06:30:00'),
(2, 1, '2025-08-20 10:00:00'),
(3, 2, '2025-08-21 11:00:00'),
(4, 1, '2025-08-22 11:00:00'),
(5, 1, '2025-08-22 12:00:00'),
(6, 1, '2025-08-22 13:00:00'),
(7, 2, '2025-08-22 14:00:00'),
(8, 2, '2025-08-22 15:00:00'),
(9, 1, '2025-08-22 16:00:00'),
(10, 2, '2025-08-22 17:00:00');

-- -----------------
-- CONSULTAS SIMPLES
-- -----------------
SELECT * FROM Usuarios;
SELECT * FROM Dispositivos;
SELECT * FROM Automatizaciones;
SELECT * FROM Registro_Actividad;
SELECT * FROM Usuario_Dispositivo;
SELECT * FROM Dispositivo_Automatizacion;

-- -----------------
-- CONSULTAS MULTITABLA
-- -----------------
-- Dispositivos con sus automatizaciones
SELECT a.nombre AS Automatizacion, d.nombre AS Dispositivo
FROM automatizaciones a
JOIN dispositivos d ON a.id_dispositivo = d.id;

-- Cantidad de automatizaciones activas por dispositivo
SELECT d.nombre AS Dispositivo, COUNT(a.id) AS Cantidad_Activadas
FROM dispositivos d
LEFT JOIN automatizaciones a ON d.id = a.id_dispositivo AND a.activa = 1
GROUP BY d.nombre;

-- Listar usuarios que tienen un dispositivo asignado a automatización
SELECT u.nombre AS Usuario, d.nombre AS Dispositivo
FROM usuarios u
JOIN automatizaciones a ON u.id = a.id_dispositivo -- simulando relación por asignación
JOIN dispositivos d ON a.id_dispositivo = d.id;

-- Mostrar dispositivos sin automatizaciones activas
SELECT nombre FROM dispositivos
WHERE id NOT IN (SELECT id_dispositivo FROM automatizaciones WHERE activa = 1);

-- -----------------
-- SUBCONSULTAS
-- -----------------
-- Usuarios cuyo nombre contiene 'Juan' (ejemplo de filtro)
SELECT nombre FROM usuarios
WHERE id IN (SELECT id FROM usuarios WHERE nombre LIKE '%Juan%');

-- Dispositivos que tienen automatizaciones activas
SELECT nombre FROM dispositivos
WHERE id IN (SELECT id_dispositivo FROM automatizaciones WHERE activa = 1);