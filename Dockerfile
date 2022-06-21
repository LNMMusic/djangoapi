# image
FROM python:3.8.5-alpine
#ENV PYTHONUNBUFFERED=1

# current dir
WORKDIR /backend

# dependencies
COPY ./requirements.txt /backend/requirements.txt

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
RUN apk add netcat-openbsd

RUN apk add --no-cache gcc musl-dev python3-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#extra
RUN pip install tzdata

# app
COPY . /backend/
EXPOSE 8000

# execute
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
