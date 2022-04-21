FROM python:3.9

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "app:app"]
