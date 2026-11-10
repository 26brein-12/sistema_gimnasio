# Sistema de Gimnasio

## ¿De qué trata el proyecto?
Este proyecto lo hice para ayudar a organizar la información de un gimnasio. Aquí se pueden manejar los socios, los planes, los entrenadores, las clases, las membresías y las inscripciones.

## ¿Qué tiene el sistema?
- **Socios:** para registrar a las personas que van al gimnasio.
- **Planes:** para guardar los planes que ofrece el gimnasio y sus precios.
- **Entrenadores:** para registrar los entrenadores.
- **Clases:** para crear las clases y asignarles un entrenador.
- **Membresías:** para saber qué plan tiene cada socio y cuándo empieza y termina.
- **Inscripciones:** para registrar a los socios en las clases.

## ¿Qué utilicé?
- Python
- Django
- SQLite

## ¿Cómo ejecutar el proyecto?
1. Descargar o clonar el proyecto.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las dependencias con este comando:

   `pip install -r requirements.txt`

4. Ejecutar las migraciones:

   `python manage.py migrate`

5. Iniciar el servidor:

   `python manage.py runserver`

6. Abrir el navegador y entrar a:

   `http://127.0.0.1:8000/`

## Panel de administrador
Para entrar al panel de administración, abre esta dirección:

`http://127.0.0.1:8000/admin/`

Necesitas tener un usuario administrador para poder ingresar.