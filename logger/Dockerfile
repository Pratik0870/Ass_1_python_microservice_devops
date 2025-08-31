FROM python:3.11-slim
WORKDIR /app
COPY logger/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY logger /app
EXPOSE 9000
CMD ["python", "app.py"]
