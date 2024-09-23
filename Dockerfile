FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y ffmpeg libsm6 libxext6

RUN ["chmod", "+x", "./start_server.sh"]

EXPOSE 8000

CMD ./start_server.sh
