FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
COPY tests/test_api.py .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest -v"]