FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
RUN apk update && \
    apk add --no-cache \
        python3-dev \
        build-base
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./sas_client /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]