FROM python:3.7.5-buster

# Workdir
ENV WORKDIR /App
WORKDIR $WORKDIR

# Install/update dependencies
RUN apt-get update && \
    apt-get install -y apt-utils autoconf build-essential curl git libssl-dev unzip vim zip gnupg wget && \
    apt-get -y install build-essential
RUN python -m pip install --upgrade pip

# Install Python libraries
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Do not stop the container
ENTRYPOINT ["tail", "-f", "/dev/null"]
