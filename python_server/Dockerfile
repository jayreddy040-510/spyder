FROM python:latest

WORKDIR /app

# install dependencies
COPY ./python_server/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./python_server .

EXPOSE 50051
CMD ["python", "server.py"]
