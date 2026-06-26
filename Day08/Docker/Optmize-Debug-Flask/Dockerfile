FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000/ || exit 1
CMD ["python", "app.py"]