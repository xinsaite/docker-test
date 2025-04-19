FROM python:3.13.3-alpine3.21
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python3","app.py"]