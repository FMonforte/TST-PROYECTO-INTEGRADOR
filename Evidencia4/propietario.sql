use proyectoIntegradorV01;

CREATE TABLE propietario (id MEDIUMINT NOT NULL AUTO_INCREMENT, Nombre varchar(30) NOT NULL, Apellido varchar(39), FechaNacimiento datetime, PRIMARY KEY (id));
     
INSERT INTO propietario (Nombre,Apellido,FechaNacimiento)
Values ('Emilio','Vera','1985-05-08');
INSERT INTO propietario (Nombre,Apellido,FechaNacimiento)
Values ('Jose','Gonzalez','1965-05-08');
INSERT INTO propietario (Nombre,Apellido,FechaNacimiento)
Values ('Pablo','Figueroa','1980-05-08');




