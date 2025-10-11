
use domotica_prueba;

insert into Usuario (nombre, mail, contraseña, rol) values
('Juan Pérez', 'juan.perez@email.com', 'contr123', 'admin'),
('María González', 'maria.gonzalez@email.com', 'contr456', 'estandar'),
('Carlos López', 'carlos.lopez@email.com', 'contr789', 'estandar'),
('Ana Martínez', 'ana.martinez@email.com', 'contr101', 'estandar'),
('Luis Rodríguez', 'luis.rodriguez@email.com', 'contr202', 'estandar'),
('Elena Sánchez', 'elena.sanchez@email.com', 'contr303', 'admin'),
('Pedro Romero', 'pedro.romero@email.com', 'contr404', 'estandar'),
('Sofía Torres', 'sofia.torres@email.com', 'contr505', 'admin'),
('Miguel Herrera', 'miguel.herrera@email.com', 'contr606', 'estandar'),
('Laura Jiménez', 'laura.jimenez@email.com', 'contr707', 'estandar');

insert into Dispositivo (nombre, tipo, estado, es_esencial) values
('Cafetera Inteligente', 'electrodoméstico', 'inactivo', FALSE),
('Televisor Sala', 'entretenimiento', 'activo', FALSE),
('Consola Juegos', 'entretenimiento', 'activo', FALSE),
('Luz Dormitorio', 'iluminación', 'activo', FALSE),
('Luz Cocina', 'iluminación', 'activo', FALSE),
('Cerradura Inteligente', 'seguridad', 'activo', TRUE),
('Sensor Movimiento', 'seguridad', 'activo', TRUE),
('Cámara Entrada', 'seguridad', 'activo', TRUE),
('Router WiFi', 'conectividad', 'activo', TRUE),
('Televisor Pieza', 'entretenimiento', 'activo', FALSE);

insert into Automatizacion (tipo, id_usuario) values
('modo ahorro', 1),
('control parental', 2),
('programar cafetera', 3);

insert into Registro_Actividad (fecha_hora, accion, id_usuario, id_dispositivo) values
('2025-09-01 07:00:00', 'encender', 3, 1),
('2025-09-01 20:00:00', 'apagar', 2, 2),
('2025-09-02 18:30:00', 'activar', 1, 6),
('2025-09-03 07:10:00', 'encender', 3, 1);

insert into Usuario_Dispositivo (id_usuario, id_dispositivo, fecha_asignacion) values
(1, 6, '2025-08-15 10:00:00'),
(3, 1, '2025-08-16 09:30:00');


insert into Dispositivo_Automatizacion (id_dispositivo, id_automatizacion, fecha_configuracion) values
(2, 1, '2025-08-20 10:00:00'),
(3, 2, '2025-08-21 11:00:00'),
(1, 3, '2025-08-22 06:30:00');



--consultas

--Esto te deja consultar por los usuarios que comienzan con letra M
select * from usuario
where nombre like "m%";

--Consulta para los dispositivos que son esenciales
select * from dispositivo 
where es_esencial = TRUE;

--Automatizacion con el nombre del usuario que la inicio
select automatizacion.id_automatizacion, automatizacion.tipo, Usuario.nombre from automatizacion
join Usuario on automatizacion.id_usuario = Usuario.id_usuario;

--Esto te deja ver las ultimas 3 acciones registradas
select accion, fecha_hora from Registro_Actividad
order by fecha_hora desc
limit 3;

--Dispositivos asignados a un usuario específico
select * from Usuario_Dispositivo
where id_usuario = 1;

--Dispositivos automatizados despues de una fecha
select * from Dispositivo_Automatizacion
where fecha_configuracion > '2025-08-21';