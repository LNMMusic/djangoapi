# image
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# current dir
WORKDIR /backend

# dependencies
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# app
COPY . /backend/
EXPOSE 8000

# execute
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
