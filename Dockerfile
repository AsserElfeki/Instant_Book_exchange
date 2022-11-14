FROM python:3.9.6-alpine

WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# make entrypoint.sh executable
RUN chmod +x ./entrypoint.sh
RUN sed -i 's/\r$//g' ./entrypoint.sh



ENTRYPOINT ["./entrypoint.sh"]
