![Django logo](https://1000marcas.net/wp-content/uploads/2021/06/Django-Logo.png)
# Desarrollo del curso de DJANGO

Realización del proyecto básico con Django. 

## Requisitos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python (versión 3.12.0)
- Django (versión 5.0.1)

## Configuración del Entorno

1. Clona el repositorio:

   ```bash
   git clone https://github.com/CristhianVM99/CURSO-DJANGO
   cd CURSO-DJANGO
   ```
2. Crea tu entorno virtual:
   ```bash
    pyenv virtualenv 3.12.0 django
   ```   
3. Activa tu entorno virtual:
   ```bash
   pyenv activate django
   ```
   <p>para verificar si esta activado tu entorno usa 'pyenv version-name'</p>
4. instala las dependencias.
    ```bash
    pip install -r requirements.txt
    ```
5. Aplica migraciones.
   ```bash
   python manage.py migrate
   ```
6. Inicia el servidor de desarrollo.
   ```bash
   python manage.py runserver
   ```
