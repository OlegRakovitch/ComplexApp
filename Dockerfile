FROM python:3.7-alpine3.8

RUN pip install aiohttp==3.3.1

COPY ./app /app

WORKDIR /app

CMD ["python", "-W", "error::RuntimeWarning", "-m", "app"]
