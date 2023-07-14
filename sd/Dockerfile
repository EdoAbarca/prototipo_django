FROM python:3.11-slim-bullseye
#RUN pip install --upgrade pip  
ENV PYTHONUNBUFFERED 1
WORKDIR /app

#COPY ./neows ./

#RUN virtualenv -p python3 env

#WORKDIR /app/neows

#RUN   ./env/Scripts/activate && \ 
#pip install django djangorestframework django-cors-headers requests pymongo && \
#python manage.py runserver 

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
