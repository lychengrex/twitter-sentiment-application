FROM python:3.8.6

WORKDIR usr/src/flask_app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p logs && touch logs/access.log logs/error.log