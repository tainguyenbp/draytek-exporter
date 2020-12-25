# Draytek exporter - Vigor exporter for hardware CPU, Memory, Build No, Version etc. written in Python with pluggable metric collectors.
This project is built with:

- Python 3.6.x

And is packaged as a Docker container. The two top level dependencies are:

- prometheus-client==0.0.21
- netmiko==3.3.0
- cryptography==2.8
- pip==9.0.3
- prometheus==0.3.0
- psutil==5.7.2



See the [requirements file](./requirements.txt) for more details.

## Prometheus

monitoring application.

To instrument our Python code we need to manipulate the metrics each
time a new HTTP request is received.

See [the application](./draytek-exporter.py) for more details.

## Building

This project is automatically built by Docker Automated Builds.

To build manually:
```
git clone https://github.com/tainguyenbp/draytek-exporter.git
cd draytek-exporter
docker build -t draytek-exporter/tainguyenbp:v1.1 .
```

## Running

Simply open port 9250 when running as a container:

`docker-comose up --build -d`

## Access URL check metrics

access url with port 9252:

`curl http://127.0.0.1:9252/metrics`

## Add config to the prometheus.yml file:

```
  - job_name: 'draytek_exporter'
    scrape_interval: 60s
    scrape_timeout: 60s
    static_configs:
    - targets: ['192.168.1.10:9252']
```

