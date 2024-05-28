# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the genetic algorithm script
CMD ["python", "python/main.py"]
