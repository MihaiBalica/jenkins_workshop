FROM python:3.10-slim

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
CMD [ "python", "app.py" ]