FROM python:3.11-slim

LABEL maintainer="Ekaterina Kudelya"
LABEL description="IT Compass - Objective IT Career Growth Tracker"
LABEL version="1.0.0"
LABEL methodology="© 2025 Ekaterina Kudelya, CC BY-ND 4.0"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY setup.sh ./
RUN chmod +x setup.sh
CMD ["python", "src/main.py"]
