# Start from a base image
FROM python:3.11-slim

# (Optional) Set a working directory
WORKDIR /app

# Copy requirements.txt and install the Python dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN pip3 install --no-cache-dir poetry
RUN poetry install

# Copy the rest of the code
COPY plugin plugin
COPY main.py .

# (Optional) Expose any ports your app uses
EXPOSE 7777

ENTRYPOINT ["python3", "main.py"]

# Specify the command to run when the container starts
CMD ["serve", "--address", "[::]:7777", "--log-format", "json", "--log-level", "info"]