FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements/production.txt
# RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
# TODO Setup gunicorn to run
