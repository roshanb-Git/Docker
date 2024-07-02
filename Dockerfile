FROM continuumio/anaconda3:latest

COPY . /usr/app/
WORKDIR /usr/app/

# Install system dependencies
RUN apt-get update && apt-get install -y python3-venv

# Create and activate virtual environment
RUN python3 -m pip install setuptools

# Upgrade pip
RUN pip install --upgrade pip

# Install numpy (and other necessary system packages if required)
RUN pip install numpy

# Install specific versions of dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose necessary ports or set other configurations
EXPOSE 5000

# Define the command to run your application
CMD [ "python", "app.py" ]
