FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the application code and start.sh file
COPY app.py start.sh requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the start.sh file executable
RUN chmod +x start.sh

# Set the command to be run when the container starts
CMD ["./start.sh"]
