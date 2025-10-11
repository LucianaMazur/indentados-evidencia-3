
create database domotica_prueba;

use domotica_prueba;

create table Usuario (
    id_usuario INT primary key auto_increment,
    nombre VARCHAR(100) not null,
    mail VARCHAR(50) not null unique,
    contraseña VARCHAR(100) not null,
    rol VARCHAR(20) not null
    );

create table Dispositivo (
    id_dispositivo INT primary key auto_increment,
    nombre VARCHAR(100) not null,
    tipo VARCHAR(50) not null,
    estado VARCHAR(50) not null,
    es_esencial BOOLEAN not null default FALSE
    );

create table Automatizacion (
    id_automatizacion INT primary key auto_increment,
    tipo VARCHAR(100) not null,
    id_usuario INT not null,
    foreign key (id_usuario) references Usuario(id_usuario)
    );

create table Registro_Actividad (
    id_registro INT primary key auto_increment,
    fecha_hora DATETIME not null default current_timestamp,
    accion VARCHAR(50) not null,
    id_usuario INT not null,
    id_dispositivo INT not null,
    foreign key (id_usuario) references Usuario(id_usuario),
    foreign key (id_dispositivo) references Dispositivo(id_dispositivo)
    );

create table Usuario_Dispositivo (
    id_usuario INT,
    id_dispositivo INT,
    fecha_asignacion DATETIME default current_timestamp,
    primary key (id_usuario, id_dispositivo),
    foreign key (id_usuario) references Usuario(id_usuario),
    foreign key (id_dispositivo) references Dispositivo(id_dispositivo)
    );

create table Dispositivo_Automatizacion (
    id_dispositivo INT,
    id_automatizacion INT,
    fecha_configuracion DATETIME default current_timestamp,
    primary key (id_dispositivo, id_automatizacion),
    foreign key (id_dispositivo) references Dispositivo(id_dispositivo),
    foreign key (id_automatizacion) references Automatizacion(id_automatizacion)
    );