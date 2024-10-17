# Dockerfile for service_a
FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install Flask and TensorFlow with compatible NumPy version
RUN pip install Flask==2.0.3 tensorflow==2.7.0 numpy==1.21.5

CMD ["python", "service_a.py"]
