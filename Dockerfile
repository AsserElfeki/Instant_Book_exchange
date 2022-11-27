FROM python:3.9-slim
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    python3-pip \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    libmagic-dev



COPY . .

#install dependencies
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# make entrypoint.sh executable
RUN chmod +x ./entrypoint.sh
RUN sed -i 's/\r$//g' ./entrypoint.sh



ENTRYPOINT ["./entrypoint.sh"]
