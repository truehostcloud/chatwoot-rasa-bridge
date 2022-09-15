FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y ffmpeg libsm6 libxext6

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "app:app", "-b 0.0.0.0"]
