FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "app:app", "-b 0.0.0.0"]
