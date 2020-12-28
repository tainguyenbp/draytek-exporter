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

## Update infor device 
Change infor ssh the device drytek:
```
git clone https://github.com/tainguyenbp/draytek-exporter.git
cd draytek-exporter
vim draytek-exporter.py
```
Find line the below and update variable host, username, password, port ssh:
```
vigor_draytek_3900 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
    'verbose': False,
    'timeout': 60,
    'global_delay_factor': 3,
    'conn_timeout': 60
}
```

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
draytek_vigor_3900_memory_usage{host="192.168.1.1"} 78
# HELP draytek_vigor_3900_metric_bootloader_version Draytek Vigor 3900 BootLoader Version
# TYPE draytek_vigor_3900_metric_bootloader_version gauge
draytek_vigor_3900_metric_bootloader_version{host="192.168.1.1"} 131
# HELP draytek_vigor_3900_metric_build_date_time Draytek Vigor 3900 Build Date Time
# TYPE draytek_vigor_3900_metric_build_date_time gauge
draytek_vigor_3900_metric_build_date_time{host="192.168.1.1"} 2020-06-05 02:32:43
# HELP draytek_vigor_3900_metric_cpu_usage Draytek Vigor 3900 CPU Usage
# TYPE draytek_vigor_3900_metric_cpu_usage gauge
draytek_vigor_3900_metric_cpu_usage{host="192.168.1.1"} 24
# HELP draytek_vigor_3900_metric_current_system_time Draytek Vigor 3900 Current System Time
# TYPE draytek_vigor_3900_metric_current_system_time gauge
draytek_vigor_3900_metric_current_system_time{host="192.168.1.1"} 28 Dec 2020 16:54:24 +0700
# HELP draytek_vigor_3900_metric_eeprom_version Draytek Vigor 3900 EEPROM Version
# TYPE draytek_vigor_3900_metric_eeprom_version gauge
draytek_vigor_3900_metric_eeprom_version{host="192.168.1.1"} 40
# HELP draytek_vigor_3900_metric_firmware_verison Draytek Vigor 3900 Firmware Version
# TYPE draytek_vigor_3900_metric_firmware_verison gauge
draytek_vigor_3900_metric_firmware_verison{host="192.168.1.1"} 1.5.1.1
# HELP draytek_vigor_3900_metric_hardware_verison Draytek Vigor 3900 Hardware Version
# TYPE draytek_vigor_3900_metric_hardware_verison gauge
draytek_vigor_3900_metric_hardware_verison{host="192.168.1.1"} 2 (M)
# HELP draytek_vigor_3900_metric_load_average1 Draytek Vigor 3900 Load Average 1 Minutes
# TYPE draytek_vigor_3900_metric_load_average1 gauge
draytek_vigor_3900_metric_load_average1{host="192.168.1.1"} 2.84
# HELP draytek_vigor_3900_metric_load_average15 Draytek Vigor 3900 Load Average 15 Minutes
# TYPE draytek_vigor_3900_metric_load_average15 gauge
draytek_vigor_3900_metric_load_average15{host="192.168.1.1"} 2.02
# HELP draytek_vigor_3900_metric_load_average5 Draytek Vigor 3900 Load Average 5 Minutes
# TYPE draytek_vigor_3900_metric_load_average5 gauge
draytek_vigor_3900_metric_load_average5{host="192.168.1.1"} 2.02
# HELP draytek_vigor_3900_metric_memory_buffer Draytek Vigor 3900 Memory Buffer
# TYPE draytek_vigor_3900_metric_memory_buffer gauge
draytek_vigor_3900_metric_memory_buffer{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_cached Draytek Vigor 3900 Memory Cached
# TYPE draytek_vigor_3900_metric_memory_cached gauge
draytek_vigor_3900_metric_memory_cached{host="192.168.1.1"} 98752
# HELP draytek_vigor_3900_metric_memory_free Draytek Vigor 3900 Memory Free
# TYPE draytek_vigor_3900_metric_memory_free gauge
draytek_vigor_3900_metric_memory_free{host="192.168.1.1"} 42128
# HELP draytek_vigor_3900_metric_memory_shards Draytek Vigor 3900 Memory Shards
# TYPE draytek_vigor_3900_metric_memory_shards gauge
draytek_vigor_3900_metric_memory_shards{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_used Draytek Vigor 3900 Memory Used
# TYPE draytek_vigor_3900_metric_memory_used gauge
draytek_vigor_3900_metric_memory_used{host="192.168.1.1"} 179768
# HELP draytek_vigor_3900_metric_model Draytek Vigor 3900 Model
# TYPE draytek_vigor_3900_metric_model gauge
draytek_vigor_3900_metric_model{host="192.168.1.1"} 3900
# HELP draytek_vigor_3900_metric_revision Draytek Vigor 3900 revision
# TYPE draytek_vigor_3900_metric_revision gauge
draytek_vigor_3900_metric_revision{host="192.168.1.1"} 8172
# HELP draytek_vigor_3900_metric_system_up_time Draytek Vigor 3900 system up time
# TYPE draytek_vigor_3900_metric_system_up_time gauge
draytek_vigor_3900_metric_system_up_time{host="192.168.1.1"} 109 days 10 hours 40 minutes 45 seconds
```
