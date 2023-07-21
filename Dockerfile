FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
COPY wsgi.py wsgi.py
COPY blog ./blog
#COPY .env ./blog/.

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]