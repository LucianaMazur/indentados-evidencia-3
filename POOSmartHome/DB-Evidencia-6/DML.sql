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
INSERT INTO dispositivos (nombre, tipo, esencial) VALUES
('Cafetera Inteligente', 'electrodoméstico', TRUE),
('Televisor Sala', 'entretenimiento', FALSE),
('Consola Juegos', 'entretenimiento', FALSE),
('Luz Dormitorio Principal', 'iluminación', TRUE),
('Luz Cocina', 'iluminación', TRUE),
('Luz Baño', 'iluminación', FALSE),
('Cerradura Inteligente', 'seguridad', FALSE),
('Sensor Movimiento Entrada', 'seguridad', TRUE),
('Cámara Puerta Principal', 'seguridad', TRUE),
('Termostato Inteligente', 'climatización', TRUE),
('Ventilador Techo Sala', 'climatización', FALSE),
('Parlante Inteligente', 'entretenimiento', FALSE);


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


INSERT INTO registro_actividad (usuario, accion, detalle) VALUES
('admin', 'Creación inicial del sistema', 'El usuario admin fue creado automáticamente.'),
('admin', 'Alta de dispositivo', 'Se registró el dispositivo "Cafetera Inteligente".'),
('admin', 'Alta de automatización', 'Se creó la automatización "Modo ahorro energético".'),
('juanp', 'Inicio de sesión', 'El usuario juanp inició sesión correctamente.'),
('mariag', 'Cambio de estado de automatización', 'La automatización "Encender al amanecer" fue desactivada.'),
('admin', 'Eliminación de dispositivo', 'El dispositivo "Ventilador Techo Sala" fue eliminado.');

--======================================================================
-- CONSULTAS SIMPLES
--======================================================================

-- Mostrar todos los registros de actividad ordenados por fecha (más recientes primero)
-- Justificación: Permite ver la trazabilidad completa de acciones del sistema
SELECT id, fecha, usuario, accion, detalle
FROM registro_actividad
ORDER BY fecha DESC;

-- Consultar las acciones realizadas por el usuario administrador
-- Justificación: Facilita la revisión de operaciones críticas del administrador del sistema
SELECT fecha, accion, detalle
FROM registro_actividad
WHERE usuario = 'admin'
ORDER BY fecha DESC;

-- Mostrar cuántas acciones realizó cada usuario
-- Justificación: Brinda un resumen de participación y uso del sistema
SELECT usuario, COUNT(*) AS Total_Acciones
FROM registro_actividad
GROUP BY usuario
ORDER BY Total_Acciones DESC;

--======================================================================
-- CONSULTAS MULTITABLA
--======================================================================

-- Mostrar los registros de actividad junto con el rol del usuario que realizó cada acción
-- Justificación: Permite analizar si las acciones fueron realizadas por administradores o usuarios estándar
SELECT 
    r.usuario AS Usuario,
    u.role AS Rol,
    r.accion AS Acción,
    r.detalle AS Detalle,
    r.fecha AS Fecha
FROM registro_actividad r
INNER JOIN usuarios u ON r.usuario = u.username
ORDER BY r.fecha DESC;

-- Listar los dispositivos que hayan sido mencionados en las acciones del registro
-- Justificación: Vincula información de registro con los dispositivos afectados
SELECT 
    d.nombre AS Dispositivo,
    r.usuario AS Usuario,
    r.accion AS Acción,
    r.fecha AS Fecha
FROM registro_actividad r
INNER JOIN dispositivos d ON r.detalle LIKE CONCAT('%', d.nombre, '%')
ORDER BY r.fecha DESC;

--======================================================================
-- SUBCONSULTAS
--======================================================================

-- Mostrar los usuarios que realizaron más de una acción registrada
-- Justificación: Identifica a los usuarios más activos dentro del sistema
SELECT usuario
FROM registro_actividad
GROUP BY usuario
HAVING COUNT(*) > 1;

-- Mostrar las acciones más recientes realizadas por cada usuario
-- Justificación: Permite ver el último evento registrado por usuario, útil para auditorías
SELECT r.usuario, r.accion, r.fecha
FROM registro_actividad r
WHERE r.fecha = (
    SELECT MAX(r2.fecha)
    FROM registro_actividad r2
    WHERE r2.usuario = r.usuario
)
ORDER BY r.fecha DESC;

-- Mostrar las acciones relacionadas con automatizaciones
-- Justificación: Permite auditar modificaciones o creaciones de automatizaciones
SELECT *
FROM registro_actividad
WHERE detalle LIKE '%automatización%'
ORDER BY fecha DESC;