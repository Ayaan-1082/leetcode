FROM python:3.9-slim

WORKDIR /app
COPY greatest.py .

ENTRYPOINT ["python", "greatest.py"]
