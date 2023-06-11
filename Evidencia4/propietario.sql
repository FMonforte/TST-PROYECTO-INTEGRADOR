use proyectoIntegradorV01;

CREATE TABLE propietario (id MEDIUMINT NOT NULL AUTO_INCREMENT, Nombre CHAR(30) NOT NULL, Apellido CHAR(39), FechaNacimiento datetime, PRIMARY KEY (id));
     
INSERT INTO Propietario ( Apellido, Nombre, FechaNacimiento) 
Values (Vera, Emilio, '05-07-1990' );


