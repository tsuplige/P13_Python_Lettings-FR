FROM python:3

ENV PYTHONBUFFER 1 

ENV PYTHONDONTWRTEBYTECODE 1

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh" ]