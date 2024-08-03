# base image
FROM python:3.10-slim

# set working directory
RUN mkdir /workspace
WORKDIR /workspace

# add current directory code to working directory
ADD . /workspace

# set default env vars
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project env vars (Optional)
# grab these with python's os.environ
ENV PORT 8888

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	tzdata \
	libopencv-dev \
	build-essential \
	libssl-dev \
	libpq-dev \
	libcurl4-gnutls-dev \
	libexpat1-dev \
	python3-setuptools \
	python3-pip \
	python3-dev \
	python3-venv \
	git \
	&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# install env dependencies
RUN pip3 install --upgrade pip \
	&& pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888

# instruction that the command below should be run when the container starts
CMD gunicorn django_face_detection.wsgi:application --bind 0.0.0.0:$PORT