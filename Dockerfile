FROM python:3.7.1-slim

WORKDIR /srv

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./fastfoodrq/ ./fastfoodrq/
COPY ./images ./images/
COPY ./manage.py ./
COPY ./db.sqlite3 ./

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
