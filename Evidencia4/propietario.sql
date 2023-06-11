use proyectoIntegradorV01;

CREATE TABLE if not exists Dispositivos (
Id_Dispositivo int primary key not null auto_increment,
Modelo varchar(20) not null, 
Numero_de_Serie varchar(25) not null, 
Direccion_de_Instalacion varchar(30),
Fecha datetime, 
Coordenadas varchar(20), 
Estado varchar(20)
);

INSERT INTO dispositivos (Modelo, Numero_de_Serie, Direccion_de_Instalacion, Fecha, Coordenadas, Estado)
values("ARDUINO", "AR202855NO", "CASTILLA 1700", '2023-01-01', 00000, "OPERATIVO");
INSERT INTO dispositivos (Modelo, Numero_de_Serie, Direccion_de_Instalacion, Fecha, Coordenadas, Estado)
values("RASPBERRY", " RP25038ry", "LEÓN 1350", '2023-02-02', 00001, "BAJA BATERÍA");
INSERT INTO dispositivos (Modelo, Numero_de_Serie, Direccion_de_Instalacion, Fecha, Coordenadas, Estado)
values("ESP32", "ESP3540032", "MURCIA 1500", '2023-03-03', 00002, "SIN CONEXIÓN");




