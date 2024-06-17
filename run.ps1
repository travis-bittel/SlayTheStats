npm run dev
python manage.py collectstatic --noinput
start firefox http://127.0.0.1:8000/query/
python manage.py runserver