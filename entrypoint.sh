# Ejecuta collectstatic para reunir archivos estáticos
python manage.py collectstatic --noinput

# Ejecuta el comando original pasado como argumentos a este script
exec "$@"