FROM python:3.6-alpine3.7

MAINTAINER tainguyenbp

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY cisco3650_exporter.py .

RUN apk --no-cache add build-base libffi-dev openssl-dev linux-headers \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --upgrade pip \
    && pip install --no-cache-dir netmiko \
    && pip install --no-cache-dir pip==9.0.3 \
    && pip install --no-cache-dir prometheus \
    && pip install --no-cache-dir psutil \
    && rm -rf /var/cache/apk/* \
    && rm -f /root/.cache

EXPOSE 9250

CMD ["/usr/src/app/cisco3650_exporter.py"]
ENTRYPOINT ["python"]
