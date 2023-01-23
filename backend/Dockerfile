# FROM python:3.8.5-slim-buster
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# Update services
RUN apt-get update && apt-get install -y &&\
    apt-get install zip unzip

# Update pip
RUN pip install --upgrade pip

WORKDIR /workspace

# Copy requirements.txt
COPY predict.py app.py download_model.py requirements.txt /workspace/

# Install requirements
RUN pip3 install -r requirements.txt

# Download and unzip model
RUN mkdir -p /workspace/models

EXPOSE ${PORT}

RUN ["python3", "download_model.py"]
# CMD ["flask", "run", "app", "-h 0.0.0.0", "-p 8334"]

RUN pwd && ls

ENTRYPOINT FLASK_APP=/workspace/app.py flask run --host=0.0.0.0 --port=8334