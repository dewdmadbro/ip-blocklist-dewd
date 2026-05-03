# Use a slim Python image as the base for the container
FROM python:bookworm
# Install necessary packages for bash, curl, and wget
RUN apt-get update && apt-get install -y bash curl wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install required Python libraries for the application
RUN pip install --no-cache-dir pandas requests ipaddress python-dotenv pysubnettree

# Set the working directory in the container
WORKDIR /app

# Download the Python script that will serve as the main application entry point
RUN wget -O __main__.py https://raw.githubusercontent.com/andrewtwin/ip-aggregator/refs/heads/main/__main__.py

# Copy necessary files to the container
COPY . /app

# Create necessary directories
RUN mkdir -p /data/geoip /data/output

# Specify the entrypoint to run the application
ENTRYPOINT [ "bash", "/app/run.sh" ]
