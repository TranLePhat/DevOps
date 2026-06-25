FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install flask
COPY api.py .
CMD ["python", "api.py"]