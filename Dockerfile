FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libmariadb-dev netcat-traditional

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY . /app/

EXPOSE 8000
ENTRYPOINT ["sh", "./entrypoint.sh"]
