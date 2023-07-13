FROM python:3.11-alpine3.18
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY ./neows ./

#RUN virtualenv -p python3 env

#WORKDIR /app/neows

#RUN   ./env/Scripts/activate && \ 
#pip install django djangorestframework django-cors-headers requests pymongo && \
#python manage.py runserver 


COPY ./requirements.txt ./

RUN pip install -r requirements.txt

#COPY ./ ./

#WORKDIR /app/neows

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]

#CMD ["sh", "entrypoint.sh"]