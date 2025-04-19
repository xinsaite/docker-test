FROM python:3.13.3-alpine3.21
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","app.py"]