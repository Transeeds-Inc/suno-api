FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
CMD [ "python", "main.py" ]
