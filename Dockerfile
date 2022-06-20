# image
FROM python3.9-slim-buster

# current dir
WORKDIR /backend

# dependencies
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# app
COPY . /backend/
EXPOSE 8080

# execute
# CMD [ "python", "manage.py", "runserver" ]