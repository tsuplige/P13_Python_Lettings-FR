FROM python:3

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN /bin/mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]