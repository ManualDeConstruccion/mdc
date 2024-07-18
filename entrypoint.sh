#!/bin/sh

# Ejecuta collectstatic para reunir archivos estáticos
python3 manage.py collectstatic --noinput

# Verifica la existencia de la carpeta y lista su contenido
if [ -d "/app/staticfiles" ]; then
    echo "La carpeta staticfiles existe y contiene los siguientes archivos:"
    ls -l /app/staticfiles
else
    echo "La carpeta staticfiles no se creó."
fi

# Ejecuta el comando original pasado como argumentos a este script
exec "$@"