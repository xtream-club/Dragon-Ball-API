# Utilizamos una imagen de Python más pequeña
FROM python:3.9-slim-buster

# Especificamos la versión de Python
ENV PYTHONUNBUFFERED=1

# Creamos un usuario no root para la aplicación
RUN adduser --system --group --no-create-home appuser

# Establecemos el directorio de trabajo en /application
WORKDIR /application

# Copiamos solo los archivos necesarios de nuestra aplicación a /application
COPY requirements.txt run.py /application/
COPY app /application/app

# Instalamos las dependencias de nuestra aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Cambiamos el propietario de los archivos de la aplicación al usuario no root
RUN chown -R appuser:appuser /application

# Establecemos la variable de entorno FLASK_APP
ENV FLASK_APP=run.py

# Exponemos el puerto 5000 para recibir peticiones
EXPOSE 5000

# Ejecutamos la aplicación con el comando flask run como el usuario no root
USER appuser
CMD ["flask", "run", "--host=0.0.0.0"]