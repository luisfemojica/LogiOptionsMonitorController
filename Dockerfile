FROM python:3.11.0-buster
COPY . usr/src/app
WORKDIR /usr/src/app

# RUN pip install -r requirements.txt

CMD ["python", "main.py"]