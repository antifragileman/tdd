# pull official base image
FROM python:3.9

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# new
# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN ls -al
RUN chmod +x /usr/src/app/entrypoint.sh
RUN apt install -y netcat


# add app
COPY . .

# new
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]