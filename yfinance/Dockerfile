# Use the official Python image as a base
FROM python:3.9

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and the config directory
COPY requirements.txt .
COPY config/ ./config/

RUN apt-get  install -y libmariadb-dev
# Upgrade pip before installing dependencies
RUN pip install --no-cache-dir --upgrade pip
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the main script
COPY script.py .


# Command to run the script
CMD ["python", "script.py"]
