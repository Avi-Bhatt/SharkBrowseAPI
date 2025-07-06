FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    curl wget gnupg libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libxshmfence1 \
    && apt-get clean

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r Requirements.txt
RUN python -m playwright install --with-deps

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
