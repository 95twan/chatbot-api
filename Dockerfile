FROM python:3.7.4

WORKDIR /APIServer

COPY requirements.txt /APIServer
RUN pip install -r requirements.txt

COPY . /APIServer

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

