# Sistema de Administraci�n de Gimnasio

##
 
Descripci�n del proyecto


Este proyecto consiste en un sistema web desarrollado para facilitar la administraci�n de un gimnasio. 
Su objetivo es organizar y gestionar la informaci�n de los socios, planes, membres�as, entrenadores, clases e inscripciones.


El sistema permite realizar operaciones de registro, consulta, edici�n y eliminaci�n de informaci�n mediante una interfaz web sencilla.



## Funcionalidades del sistema



El sistema cuenta con los siguientes m�dulos:


- **Socios:** permite registrar, consultar, editar y eliminar socios.

- **Planes:** permite administrar los planes ofrecidos por el gimnasio, sus precios y duraci�n.

- **Membres�as:** permite asignar planes a los socios y gestionar las fechas de inicio y finalizaci�n.

- **Entrenadores:** permite registrar y administrar la informaci�n de los entrenadores.

- **Clases:** permite crear clases, establecer horarios, definir cupos y asignar entrenadores.

- **Inscripciones:** permite registrar socios en las diferentes clases y administrar sus inscripciones.



## Tecnolog�as utilizadas


- Python

- Django 4.2

- SQLite

- HTML

- CSS

- Bootstrap 5



## Estructura del proyecto


El proyecto est� organizado en aplicaciones independientes para facilitar su mantenimiento:


- `socios/`

- `plan/`

- `membresias/`

- `entrenador/`

- `clase/`

- `inscripcion/`

- `gimnasio/`

- `templates/`

- `docs/`

En la carpeta `docs/` se encuentran los diagramas del sistema:


- `diagrama_actores.png`

- `diagrama_er.png`



## Instalaci�n y ejecuci�n


1. Descargar o clonar el repositorio.

2. Abrir una terminal en la carpeta principal del proyecto.

3. Crear el entorno virtual:

  
 ```bash
   py -m venv venv
 
 
 ```

4. Instalar las dependencias:

   
```bash
   .\venv\Scripts\python.exe
 -m pip install 
-r requirements.txt
   

```

5. Ejecutar las migraciones:

   
```bash
   .\venv\Scripts\python.exe manage.py migrate
 
 
 ```

6. Iniciar el servidor:

  
 ```bash
   .\venv\Scripts\python.exe manage.py runserver


   ```

7. Abrir el navegador e ingresar a:


   `http://127.0.0.1:8000/`



## Panel de administraci�n



Para ingresar al panel administrativo de Django, utilizar la siguiente direcci�n:



`http://127.0.0.1:8000/admin/`

Es necesario contar con un usuario administrador.

 Si todav�a no existe, se puede crear con el siguiente comando:


```bash
.\venv\Scripts\python.exe manage.py createsuperuser
```



## Autor�a


Proyecto acad�mico desarrollado como sistema de administraci�n de gimnasio.

