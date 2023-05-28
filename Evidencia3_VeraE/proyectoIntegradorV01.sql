
CREATE DATABASE proyectoIntegradorV01;
use proyectoIntegradorV01;

CREATE TABLE Persona ( DNI int(8), Nombre varchar (50), Telefono int (15));
CREATE TABLE Animal ( Raza varchar(29), Nombre varchar (50), Fecha_Nacimiento datetime );

insert into Persona (Dni, Nombre, Telefono)
values(31646323, 'Emilio Vera' , 15);
insert into Persona (Dni, Nombre, Telefono)
values(28757896, 'Valeria Givaudant' , 12);
insert into Persona (Dni, Nombre, Telefono)
values(29564898, 'Yamil' , 12);
insert into Persona (Dni, Nombre, Telefono)
values(30646585, 'Jose' , 231);
INSERT INTO proyectoIntegradorV01.animal (Raza, Nombre, Fecha_Nacimiento)
VALUES( 'PitBull', 'Firulais' , '2023-03-08');

SELECT * from proyectoIntegrador01.persona

 
