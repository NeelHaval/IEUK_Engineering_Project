# Ensure python is already installed
FROM python:3.11

# Use this docker container as the primary working directory
WORKDIR /project

# Transfer files to container
COPY . /project

# Run commands on external local machine to install dependencies
RUN pip install -r dependencies.txt

# Script may be run freely on local machine
CMD ["python", "anomaly_detection.py"]