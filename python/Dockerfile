FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN black .
RUN isort .
CMD ["pytest"]