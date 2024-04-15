FROM python:3.10.9

# Create a work directory in the container
WORKDIR /app

# Copy the content of requirements.txt into the work directory
COPY requirements.txt /app/requirements.txt

# Install packages from requirements.txt
RUN python -m pip install --timeout 300000 -r requirements.txt

# Copy all files into the working directory
COPY . /app

# Expose port 8077
EXPOSE 8077

# Run the FastApi application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8077"]
