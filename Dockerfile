FROM python:3.12

COPY ./app /usr/local/app
WORKDIR /usr/local/app

RUN pip install -e .

CMD ["python","app.py"]
