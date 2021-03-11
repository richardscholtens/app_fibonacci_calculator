release: flask db upgrade
web: gunicorn application_fibonacci_calculator.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
