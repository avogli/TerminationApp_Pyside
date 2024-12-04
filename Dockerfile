

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgtk-3-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y x11-apps

# Copy the local project files to the container
COPY . .

# Install Python dependencies
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  --no-cache-dir -r requirements.txt
# Set the environment variable for PySide6
ENV QT_QPA_PLATFORM offscreen
ENV QT_LOGGING_RULES="qt.qpa.plugin=false"


# Expose the port on which your app runs, if applicable
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
