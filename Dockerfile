FROM python:3.6-alpine3.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk --no-cache add build-base libffi-dev openssl-dev linux-headers \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --upgrade pip \
    && pip install cryptography==2.8 \
    && pip install --no-cache-dir netmiko \
    && pip install pip==9.0.3 \
    && pip install prometheus \
    && pip install psutil

COPY draytek_exporter.py .
EXPOSE 9252
CMD [ "python", "draytek_exporter.py"]

