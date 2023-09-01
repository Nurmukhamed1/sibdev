# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy your Django application code into the container
COPY . /code/

## Expose the port the application runs on
#EXPOSE 8000
#
## Start the Django application
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
