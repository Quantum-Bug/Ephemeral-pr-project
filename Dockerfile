# Dockerfile
FROM python:3.9-slim

WORKDIR /code

#copy requirement and install the dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./app /code/app

# Expose the port FastAPI runs on
EXPOSE 8080

#Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
