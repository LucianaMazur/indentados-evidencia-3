USE poosmarthome;

--============================================================================================
-- INSERCIÓN DE DATOS INICIALES



-- TABLA: usuarios

-- Usuario administrador predeterminado y usuarios estándar de ejemplo
INSERT INTO usuarios (username, password, nombre, email, role, activo) VALUES
('admin', 'admin123', 'Administrador Sistema', 'admin@smarthome.com', 'admin', TRUE),
('juanp', 'pass123', 'Juan Pérez', 'juan.perez@email.com', 'standard', TRUE),
('mariag', 'pass456', 'María González', 'maria.gonzalez@email.com', 'standard', TRUE),
('carlosl', 'pass789', 'Carlos López', 'carlos.lopez@email.com', 'standard', TRUE),
('anam', 'pass101', 'Ana Martínez', 'ana.martinez@email.com', 'standard', TRUE),
('luisr', 'pass202', 'Luis Rodríguez', 'luis.rodriguez@email.com', 'standard', TRUE),
('elenas', 'pass303', 'Elena Sánchez', 'elena.sanchez@email.com', 'admin', TRUE),
('pedror', 'pass404', 'Pedro Romero', 'pedro.romero@email.com', 'standard', TRUE),
('sofiat', 'pass505', 'Sofía Torres', 'sofia.torres@email.com', 'standard', TRUE),
('miguelh', 'pass606', 'Miguel Herrera', 'miguel.herrera@email.com', 'standard', FALSE),
('lauraj', 'pass707', 'Laura Jiménez', 'laura.jimenez@email.com', 'standard', TRUE);


-- TABLA: dispositivos

-- Dispositivos disponibles en el sistema
INSERT INTO dispositivos (nombre, tipo) VALUES
('Cafetera Inteligente', 'electrodoméstico'),
('Televisor Sala', 'entretenimiento'),
('Consola Juegos', 'entretenimiento'),
('Luz Dormitorio Principal', 'iluminación'),
('Luz Cocina', 'iluminación'),
('Luz Baño', 'iluminación'),
('Cerradura Inteligente', 'seguridad'),
('Sensor Movimiento Entrada', 'seguridad'),
('Cámara Puerta Principal', 'seguridad'),
('Termostato Inteligente', 'climatización'),
('Ventilador Techo Sala', 'climatización'),
('Parlante Inteligente', 'entretenimiento');


-- TABLA: automatizaciones

-- Automatizaciones configuradas para los dispositivos
INSERT INTO automatizaciones (nombre, id_dispositivo, activa) VALUES
('Encender al amanecer', 4, TRUE),
('Apagar al salir', 4, TRUE),
('Modo ahorro energético', 2, TRUE),
('Control parental nocturno', 3, TRUE),
('Encender con movimiento', 8, TRUE),
('Preparar café matutino', 1, TRUE),
('Clima automático', 10, TRUE),
('Seguridad perimetral', 9, TRUE),
('Iluminación inteligente cocina', 5, FALSE),
('Ventilación automática', 11, TRUE),
('Cerrar al dormir', 7, TRUE),
('Música ambiente', 12, FALSE);

--=========================================================================
-- CONSULTAS SIMPLES

-- Consulta: Todos los usuarios
SELECT * FROM usuarios;

-- Consulta: Todos los dispositivos
SELECT * FROM dispositivos;

-- Consulta: Todas las automatizaciones
SELECT * FROM automatizaciones;

--=======================================================================================
-- CONSULTAS MULTITABLA

-- Listar todos los dispositivos con sus automatizaciones asociadas
-- Justificacion: Permite al usuario ver qué automatizaciones tiene configurado cada dispositivo

SELECT 
    d.nombre AS Dispositivo,
    d.tipo AS Tipo_Dispositivo,
    a.nombre AS Automatizacion,
    CASE WHEN a.activa = 1 THEN 'Activa' ELSE 'Inactiva' END AS Estado
FROM dispositivos d
INNER JOIN automatizaciones a ON d.id = a.id_dispositivo
ORDER BY d.nombre, a.nombre;


-- Contar cuántas automatizaciones activas tiene cada tipo de dispositivo
-- Justificacion:: Permite identificar qué categorías de dispositivos tienen más automatización
-- es util para analisis de uso del sistema

SELECT 
    d.tipo AS Tipo_Dispositivo,
    COUNT(a.id) AS Total_Automatizaciones_Activas
FROM dispositivos d
LEFT JOIN automatizaciones a ON d.id = a.id_dispositivo AND a.activa = 1
GROUP BY d.tipo
ORDER BY Total_Automatizaciones_Activas DESC;


-- Listar dispositivos de iluminación con sus automatizaciones
-- Justificacion: Filtro específico para gestionar la iluminación del hogar

SELECT 
    d.nombre AS Dispositivo_Luz,
    a.nombre AS Automatizacion,
    CASE WHEN a.activa = 1 THEN 'Activa' ELSE 'Inactiva' END AS Estado
FROM dispositivos d
LEFT JOIN automatizaciones a ON d.id = a.id_dispositivo
WHERE d.tipo = 'iluminación'
ORDER BY d.nombre;


-- Dispositivos de seguridad con automatizaciones activas
-- Justificacion: Consulta para verificar que los sistemas de seguridad
-- estén correctamente automatizados y activos

SELECT 
    d.nombre AS Dispositivo_Seguridad,
    a.nombre AS Automatizacion_Activa
FROM dispositivos d
INNER JOIN automatizaciones a ON d.id = a.id_dispositivo
WHERE d.tipo = 'seguridad' AND a.activa = 1
ORDER BY d.nombre;


--=======================================================================
--SUBCONSULTAS

-- Listar dispositivos que no tienen ninguna automatización configurada
-- Justificacion: Identifica dispositivos sin configurar, ayudando a los usuarios
-- a aprovechar mejor las funcionalidades del sistema

SELECT 
    nombre AS Dispositivo_Sin_Automatizar,
    tipo AS Tipo
FROM dispositivos
WHERE id NOT IN (
    SELECT DISTINCT id_dispositivo 
    FROM automatizaciones
)
ORDER BY tipo, nombre;

-- Listar tipos de dispositivos que tienen al menos una automatizacion activa
-- Justificacion: Permite identificar que categorías de dispositivos están siendo
-- utilizadas activamente, util para estadísticas de uso

SELECT DISTINCT tipo AS Tipos_Con_Automatizacion_Activa
FROM dispositivos
WHERE id IN (
    SELECT id_dispositivo 
    FROM automatizaciones 
    WHERE activa = 1
)
ORDER BY tipo;