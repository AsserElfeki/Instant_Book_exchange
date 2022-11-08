# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . .

# sed -i <mod/regex//mod> (delete carriage-return globally)
RUN sed -i 's/\r$//g' ./entrypoint.sh && chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

