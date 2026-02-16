FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN chmod +x app.py

CMD ["python3", "app.py"]
