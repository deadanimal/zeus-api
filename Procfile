web: gunicorn zeusapi.wsgi -w 4 --max-requests 100
worker: celery -A  zeusapi worker --concurrency=8 -Ofair
beat: celery -A zeusapi beat
