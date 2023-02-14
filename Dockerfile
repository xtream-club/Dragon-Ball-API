# Utilizamos una imagen de Python como base
FROM python:3.9-alpine

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de nuestra aplicación a /app
COPY . .

# Instalamos las dependencias de nuestra aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Establecemos la variable de entorno FLASK_APP
ENV FLASK_APP=run.py

# Exponemos el puerto 5000 para recibir peticiones
EXPOSE 5000

# Ejecutamos la aplicación con el comando flask run
CMD ["flask", "run", "--host=0.0.0.0"]