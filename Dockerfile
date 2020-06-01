FROM python:3.6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./ /usr/src/app

RUN apt-get update && apt-get -y install cmake

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD [ "python", "./run.py" ]