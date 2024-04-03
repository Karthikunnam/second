# Use an official Python runtime as a parent image
FROM python:3.9



# Set the working directory in the container
WORKDIR /app



# Install dependencies
RUN pip install django
RUN pip install mysql-connector

# Copy the current directory contents into the container at /app
COPY  proj2 /app/

# Expose port 8000 to allow communication to/from the container
EXPOSE 8000

# Run the Django development server
CMD ["python", "/app/proj2/manage.py", "runserver", "0.0.0.0:8000"]

