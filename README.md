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

Simply open port 9252 when running as a container:

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
## metric collects:

```
# HELP draytek_vigor_3900_memory_usage Draytek Vigor 3900 Memory Usage
# TYPE draytek_vigor_3900_memory_usage gauge
draytek_vigor_3900_memory_usage{host="192.168.1.1"} 81
# HELP draytek_vigor_3900_metric_build_date_time Draytek Vigor 3900 Build Date Time
# TYPE draytek_vigor_3900_metric_build_date_time gauge
draytek_vigor_3900_metric_build_date_time{host="192.168.1.1"} 2020-06-05 02:32:43
# HELP draytek_vigor_3900_metric_cpu_usage Draytek Vigor 3900 CPU Usage
# TYPE draytek_vigor_3900_metric_cpu_usage gauge
draytek_vigor_3900_metric_cpu_usage{host="192.168.1.1"} 22
# HELP draytek_vigor_3900_metric_firmware_verison Draytek Vigor 3900 Firmware Version
# TYPE draytek_vigor_3900_metric_firmware_verison gauge
draytek_vigor_3900_metric_firmware_verison{host="192.168.1.1"} 1.5.1.1
# HELP draytek_vigor_3900_metric_hardware_verison Draytek Vigor 3900 Hardware Version
# TYPE draytek_vigor_3900_metric_hardware_verison gauge
draytek_vigor_3900_metric_hardware_verison{host="192.168.1.1"} 2 (M)
# HELP draytek_vigor_3900_metric_model Draytek Vigor 3900 Model
# TYPE draytek_vigor_3900_metric_model gauge
draytek_vigor_3900_metric_model{host="192.168.1.1"} 3900
```
