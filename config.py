# config.py

celery_broker='redis://localhost:6379/0'
celery_backend = 'redis://localhost:6379/0'


BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 1} 