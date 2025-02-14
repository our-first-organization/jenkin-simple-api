FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8081

CMD ["python", "app.py"]
