FROM python:3.8.5-slim-buster

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

RUN ["python3", "download_model.py"]
CMD ["python3", "predict.py"]