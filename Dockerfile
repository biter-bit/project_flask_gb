FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
COPY wsgi.py wsgi.py
COPY blog ./blog

ENV SQLALCHEMY_DATABASE_URI=postgresql://user:password@pg:5432/blog
ENV CONFIG_NAME=DevConfig

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]