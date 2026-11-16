# Sistema de Administración de Gimnasio

## Descripción del proyecto

Este proyecto consiste en un sistema web desarrollado para facilitar la administración de un gimnasio. Su objetivo es organizar y gestionar la información de los socios, planes, membresías, entrenadores, clases e inscripciones.

El sistema permite realizar operaciones de registro, consulta, edición y eliminación de información mediante una interfaz web sencilla.

## Funcionalidades del sistema

El sistema cuenta con los siguientes módulos:

- **Socios:** permite registrar, consultar, editar y eliminar socios.
- **Planes:** permite administrar los planes ofrecidos por el gimnasio, sus precios y duración.
- **Membresías:** permite asignar planes a los socios y gestionar las fechas de inicio y finalización.
- **Entrenadores:** permite registrar y administrar la información de los entrenadores.
- **Clases:** permite crear clases, establecer horarios, definir cupos y asignar entrenadores.
- **Inscripciones:** permite registrar socios en las diferentes clases y administrar sus inscripciones.

## Tecnologías utilizadas

- Python
- Django 4.2
- SQLite
- HTML
- CSS
- Bootstrap 5

## Estructura del proyecto

El proyecto está organizado en aplicaciones independientes para facilitar su mantenimiento:

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

- `Diagrama.png`
- `diagrama_er.png`

## Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Crear el entorno virtual:

```bash
py -m venv venv
```

4. Instalar las dependencias:

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
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

## Panel de administración

Para ingresar al panel administrativo de Django, utilizar la siguiente dirección:

`http://127.0.0.1:8000/admin/`

Es necesario contar con un usuario administrador. Si todavía no existe, se puede crear con el siguiente comando:

```bash
.\venv\Scripts\python.exe manage.py createsuperuser
```

## Autoría

Proyecto académico desarrollado como sistema de administración de gimnasio.