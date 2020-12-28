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
draytek_vigor_3900_memory_usage{host="192.168.1.1"} 77
# HELP draytek_vigor_3900_metric_bootloader_version Draytek Vigor 3900 BootLoader Version
# TYPE draytek_vigor_3900_metric_bootloader_version gauge
draytek_vigor_3900_metric_bootloader_version{host="192.168.1.1"} 131
# HELP draytek_vigor_3900_metric_build_date_time Draytek Vigor 3900 Build Date Time
# TYPE draytek_vigor_3900_metric_build_date_time gauge
draytek_vigor_3900_metric_build_date_time{host="192.168.1.1"} 2020-06-05 02:32:43
# HELP draytek_vigor_3900_metric_command_process_top_1 Draytek Vigor 3900 command process top 1
# TYPE draytek_vigor_3900_metric_command_process_top_1 gauge
draytek_vigor_3900_metric_command_process_top_1{host="192.168.1.1"} conn_dect
# HELP draytek_vigor_3900_metric_command_process_top_10 Draytek Vigor 3900 command process top 10
# TYPE draytek_vigor_3900_metric_command_process_top_10 gauge
draytek_vigor_3900_metric_command_process_top_10{host="192.168.1.1"} openvpn
# HELP draytek_vigor_3900_metric_command_process_top_2 Draytek Vigor 3900 command process top 2
# TYPE draytek_vigor_3900_metric_command_process_top_2 gauge
draytek_vigor_3900_metric_command_process_top_2{host="192.168.1.1"} top
# HELP draytek_vigor_3900_metric_command_process_top_3 Draytek Vigor 3900 command process top 3
# TYPE draytek_vigor_3900_metric_command_process_top_3 gauge
draytek_vigor_3900_metric_command_process_top_3{host="192.168.1.1"} sslproxy
# HELP draytek_vigor_3900_metric_command_process_top_4 Draytek Vigor 3900 command process top 4
# TYPE draytek_vigor_3900_metric_command_process_top_4 gauge
draytek_vigor_3900_metric_command_process_top_4{host="192.168.1.1"} clish
# HELP draytek_vigor_3900_metric_command_process_top_5 Draytek Vigor 3900 command process top 5
# TYPE draytek_vigor_3900_metric_command_process_top_5 gauge
draytek_vigor_3900_metric_command_process_top_5{host="192.168.1.1"} cmm
# HELP draytek_vigor_3900_metric_command_process_top_6 Draytek Vigor 3900 command process top 6
# TYPE draytek_vigor_3900_metric_command_process_top_6 gauge
draytek_vigor_3900_metric_command_process_top_6{host="192.168.1.1"} lighttpd
# HELP draytek_vigor_3900_metric_command_process_top_7 Draytek Vigor 3900 command process top 7
# TYPE draytek_vigor_3900_metric_command_process_top_7 gauge
draytek_vigor_3900_metric_command_process_top_7{host="192.168.1.1"} xl2tpd
# HELP draytek_vigor_3900_metric_command_process_top_8 Draytek Vigor 3900 command process top 8
# TYPE draytek_vigor_3900_metric_command_process_top_8 gauge
draytek_vigor_3900_metric_command_process_top_8{host="192.168.1.1"} snmpd
# HELP draytek_vigor_3900_metric_command_process_top_9 Draytek Vigor 3900 command process top 9
# TYPE draytek_vigor_3900_metric_command_process_top_9 gauge
draytek_vigor_3900_metric_command_process_top_9{host="192.168.1.1"} dhcpd
# HELP draytek_vigor_3900_metric_cpu_process_top_1 Draytek Vigor 3900 cpu process top 1
# TYPE draytek_vigor_3900_metric_cpu_process_top_1 gauge
draytek_vigor_3900_metric_cpu_process_top_1{host="192.168.1.1"} 5.8
# HELP draytek_vigor_3900_metric_cpu_process_top_10 Draytek Vigor 3900 cpu process top 10
# TYPE draytek_vigor_3900_metric_cpu_process_top_10 gauge
draytek_vigor_3900_metric_cpu_process_top_10{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_2 Draytek Vigor 3900 cpu process top 2
# TYPE draytek_vigor_3900_metric_cpu_process_top_2 gauge
draytek_vigor_3900_metric_cpu_process_top_2{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_cpu_process_top_3 Draytek Vigor 3900 cpu process top 3
# TYPE draytek_vigor_3900_metric_cpu_process_top_3 gauge
draytek_vigor_3900_metric_cpu_process_top_3{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_4 Draytek Vigor 3900 cpu process top 4
# TYPE draytek_vigor_3900_metric_cpu_process_top_4 gauge
draytek_vigor_3900_metric_cpu_process_top_4{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_5 Draytek Vigor 3900 cpu process top 5
# TYPE draytek_vigor_3900_metric_cpu_process_top_5 gauge
draytek_vigor_3900_metric_cpu_process_top_5{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_6 Draytek Vigor 3900 cpu process top 6
# TYPE draytek_vigor_3900_metric_cpu_process_top_6 gauge
draytek_vigor_3900_metric_cpu_process_top_6{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_7 Draytek Vigor 3900 cpu process top 7
# TYPE draytek_vigor_3900_metric_cpu_process_top_7 gauge
draytek_vigor_3900_metric_cpu_process_top_7{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_8 Draytek Vigor 3900 cpu process top 8
# TYPE draytek_vigor_3900_metric_cpu_process_top_8 gauge
draytek_vigor_3900_metric_cpu_process_top_8{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_9 Draytek Vigor 3900 cpu process top 9
# TYPE draytek_vigor_3900_metric_cpu_process_top_9 gauge
draytek_vigor_3900_metric_cpu_process_top_9{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_usage Draytek Vigor 3900 CPU Usage
# TYPE draytek_vigor_3900_metric_cpu_usage gauge
draytek_vigor_3900_metric_cpu_usage{host="192.168.1.1"} 19
# HELP draytek_vigor_3900_metric_current_system_time Draytek Vigor 3900 Current System Time
# TYPE draytek_vigor_3900_metric_current_system_time gauge
draytek_vigor_3900_metric_current_system_time{host="192.168.1.1"} 28 Dec 2020 21:52:54 +0700
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
draytek_vigor_3900_metric_load_average1{host="192.168.1.1"} 1.71
# HELP draytek_vigor_3900_metric_load_average15 Draytek Vigor 3900 Load Average 15 Minutes
# TYPE draytek_vigor_3900_metric_load_average15 gauge
draytek_vigor_3900_metric_load_average15{host="192.168.1.1"} 1.02
# HELP draytek_vigor_3900_metric_load_average5 Draytek Vigor 3900 Load Average 5 Minutes
# TYPE draytek_vigor_3900_metric_load_average5 gauge
draytek_vigor_3900_metric_load_average5{host="192.168.1.1"} 1.28
# HELP draytek_vigor_3900_metric_memory_buffer Draytek Vigor 3900 Memory Buffer
# TYPE draytek_vigor_3900_metric_memory_buffer gauge
draytek_vigor_3900_metric_memory_buffer{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_cached Draytek Vigor 3900 Memory Cached
# TYPE draytek_vigor_3900_metric_memory_cached gauge
draytek_vigor_3900_metric_memory_cached{host="192.168.1.1"} 97416
# HELP draytek_vigor_3900_metric_memory_free Draytek Vigor 3900 Memory Free
# TYPE draytek_vigor_3900_metric_memory_free gauge
draytek_vigor_3900_metric_memory_free{host="192.168.1.1"} 49860
# HELP draytek_vigor_3900_metric_memory_process_top_1 Draytek Vigor 3900 memory process top 1
# TYPE draytek_vigor_3900_metric_memory_process_top_1 gauge
draytek_vigor_3900_metric_memory_process_top_1{host="192.168.1.1"} 0.3
# HELP draytek_vigor_3900_metric_memory_process_top_10 Draytek Vigor 3900 memmory process top 10
# TYPE draytek_vigor_3900_metric_memory_process_top_10 gauge
draytek_vigor_3900_metric_memory_process_top_10{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_process_top_2 Draytek Vigor 3900 memmory process top 2
# TYPE draytek_vigor_3900_metric_memory_process_top_2 gauge
draytek_vigor_3900_metric_memory_process_top_2{host="192.168.1.1"} 0.2
# HELP draytek_vigor_3900_metric_memory_process_top_3 Draytek Vigor 3900 memory process top 3
# TYPE draytek_vigor_3900_metric_memory_process_top_3 gauge
draytek_vigor_3900_metric_memory_process_top_3{host="192.168.1.1"} 4.1
# HELP draytek_vigor_3900_metric_memory_process_top_4 Draytek Vigor 3900 memmory process top 4
# TYPE draytek_vigor_3900_metric_memory_process_top_4 gauge
draytek_vigor_3900_metric_memory_process_top_4{host="192.168.1.1"} 2.4
# HELP draytek_vigor_3900_metric_memory_process_top_5 Draytek Vigor 3900 memory process top 5
# TYPE draytek_vigor_3900_metric_memory_process_top_5 gauge
draytek_vigor_3900_metric_memory_process_top_5{host="192.168.1.1"} 2.3
# HELP draytek_vigor_3900_metric_memory_process_top_6 Draytek Vigor 3900 memmory process top 6
# TYPE draytek_vigor_3900_metric_memory_process_top_6 gauge
draytek_vigor_3900_metric_memory_process_top_6{host="192.168.1.1"} 1.8
# HELP draytek_vigor_3900_metric_memory_process_top_7 Draytek Vigor 3900 memory process top 7
# TYPE draytek_vigor_3900_metric_memory_process_top_7 gauge
draytek_vigor_3900_metric_memory_process_top_7{host="192.168.1.1"} 1.1
# HELP draytek_vigor_3900_metric_memory_process_top_8 Draytek Vigor 3900 memmory process top 8
# TYPE draytek_vigor_3900_metric_memory_process_top_8 gauge
draytek_vigor_3900_metric_memory_process_top_8{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_process_top_9 Draytek Vigor 3900 memory process top 9
# TYPE draytek_vigor_3900_metric_memory_process_top_9 gauge
draytek_vigor_3900_metric_memory_process_top_9{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_shards Draytek Vigor 3900 Memory Shards
# TYPE draytek_vigor_3900_metric_memory_shards gauge
draytek_vigor_3900_metric_memory_shards{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_used Draytek Vigor 3900 Memory Used
# TYPE draytek_vigor_3900_metric_memory_used gauge
draytek_vigor_3900_metric_memory_used{host="192.168.1.1"} 172036
# HELP draytek_vigor_3900_metric_model Draytek Vigor 3900 Model
# TYPE draytek_vigor_3900_metric_model gauge
draytek_vigor_3900_metric_model{host="192.168.1.1"} 3900
# HELP draytek_vigor_3900_metric_revision Draytek Vigor 3900 revision
# TYPE draytek_vigor_3900_metric_revision gauge
draytek_vigor_3900_metric_revision{host="192.168.1.1"} 8172
# HELP draytek_vigor_3900_metric_system_up_time Draytek Vigor 3900 system up time
# TYPE draytek_vigor_3900_metric_system_up_time gauge
draytek_vigor_3900_metric_system_up_time{host="192.168.1.1"} 109 days 15 hours 39 minutes 16 seconds# HELP draytek_vigor_3900_memory_usage Draytek Vigor 3900 Memory Usage
# TYPE draytek_vigor_3900_memory_usage gauge
draytek_vigor_3900_memory_usage{host="192.168.1.1"} 77
# HELP draytek_vigor_3900_metric_bootloader_version Draytek Vigor 3900 BootLoader Version
# TYPE draytek_vigor_3900_metric_bootloader_version gauge
draytek_vigor_3900_metric_bootloader_version{host="192.168.1.1"} 131
# HELP draytek_vigor_3900_metric_build_date_time Draytek Vigor 3900 Build Date Time
# TYPE draytek_vigor_3900_metric_build_date_time gauge
draytek_vigor_3900_metric_build_date_time{host="192.168.1.1"} 2020-06-05 02:32:43
# HELP draytek_vigor_3900_metric_command_process_top_1 Draytek Vigor 3900 command process top 1
# TYPE draytek_vigor_3900_metric_command_process_top_1 gauge
draytek_vigor_3900_metric_command_process_top_1{host="192.168.1.1"} conn_dect
# HELP draytek_vigor_3900_metric_command_process_top_10 Draytek Vigor 3900 command process top 10
# TYPE draytek_vigor_3900_metric_command_process_top_10 gauge
draytek_vigor_3900_metric_command_process_top_10{host="192.168.1.1"} openvpn
# HELP draytek_vigor_3900_metric_command_process_top_2 Draytek Vigor 3900 command process top 2
# TYPE draytek_vigor_3900_metric_command_process_top_2 gauge
draytek_vigor_3900_metric_command_process_top_2{host="192.168.1.1"} top
# HELP draytek_vigor_3900_metric_command_process_top_3 Draytek Vigor 3900 command process top 3
# TYPE draytek_vigor_3900_metric_command_process_top_3 gauge
draytek_vigor_3900_metric_command_process_top_3{host="192.168.1.1"} sslproxy
# HELP draytek_vigor_3900_metric_command_process_top_4 Draytek Vigor 3900 command process top 4
# TYPE draytek_vigor_3900_metric_command_process_top_4 gauge
draytek_vigor_3900_metric_command_process_top_4{host="192.168.1.1"} clish
# HELP draytek_vigor_3900_metric_command_process_top_5 Draytek Vigor 3900 command process top 5
# TYPE draytek_vigor_3900_metric_command_process_top_5 gauge
draytek_vigor_3900_metric_command_process_top_5{host="192.168.1.1"} cmm
# HELP draytek_vigor_3900_metric_command_process_top_6 Draytek Vigor 3900 command process top 6
# TYPE draytek_vigor_3900_metric_command_process_top_6 gauge
draytek_vigor_3900_metric_command_process_top_6{host="192.168.1.1"} lighttpd
# HELP draytek_vigor_3900_metric_command_process_top_7 Draytek Vigor 3900 command process top 7
# TYPE draytek_vigor_3900_metric_command_process_top_7 gauge
draytek_vigor_3900_metric_command_process_top_7{host="192.168.1.1"} xl2tpd
# HELP draytek_vigor_3900_metric_command_process_top_8 Draytek Vigor 3900 command process top 8
# TYPE draytek_vigor_3900_metric_command_process_top_8 gauge
draytek_vigor_3900_metric_command_process_top_8{host="192.168.1.1"} snmpd
# HELP draytek_vigor_3900_metric_command_process_top_9 Draytek Vigor 3900 command process top 9
# TYPE draytek_vigor_3900_metric_command_process_top_9 gauge
draytek_vigor_3900_metric_command_process_top_9{host="192.168.1.1"} dhcpd
# HELP draytek_vigor_3900_metric_cpu_process_top_1 Draytek Vigor 3900 cpu process top 1
# TYPE draytek_vigor_3900_metric_cpu_process_top_1 gauge
draytek_vigor_3900_metric_cpu_process_top_1{host="192.168.1.1"} 5.8
# HELP draytek_vigor_3900_metric_cpu_process_top_10 Draytek Vigor 3900 cpu process top 10
# TYPE draytek_vigor_3900_metric_cpu_process_top_10 gauge
draytek_vigor_3900_metric_cpu_process_top_10{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_2 Draytek Vigor 3900 cpu process top 2
# TYPE draytek_vigor_3900_metric_cpu_process_top_2 gauge
draytek_vigor_3900_metric_cpu_process_top_2{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_cpu_process_top_3 Draytek Vigor 3900 cpu process top 3
# TYPE draytek_vigor_3900_metric_cpu_process_top_3 gauge
draytek_vigor_3900_metric_cpu_process_top_3{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_4 Draytek Vigor 3900 cpu process top 4
# TYPE draytek_vigor_3900_metric_cpu_process_top_4 gauge
draytek_vigor_3900_metric_cpu_process_top_4{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_5 Draytek Vigor 3900 cpu process top 5
# TYPE draytek_vigor_3900_metric_cpu_process_top_5 gauge
draytek_vigor_3900_metric_cpu_process_top_5{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_6 Draytek Vigor 3900 cpu process top 6
# TYPE draytek_vigor_3900_metric_cpu_process_top_6 gauge
draytek_vigor_3900_metric_cpu_process_top_6{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_7 Draytek Vigor 3900 cpu process top 7
# TYPE draytek_vigor_3900_metric_cpu_process_top_7 gauge
draytek_vigor_3900_metric_cpu_process_top_7{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_8 Draytek Vigor 3900 cpu process top 8
# TYPE draytek_vigor_3900_metric_cpu_process_top_8 gauge
draytek_vigor_3900_metric_cpu_process_top_8{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_process_top_9 Draytek Vigor 3900 cpu process top 9
# TYPE draytek_vigor_3900_metric_cpu_process_top_9 gauge
draytek_vigor_3900_metric_cpu_process_top_9{host="192.168.1.1"} 0.0
# HELP draytek_vigor_3900_metric_cpu_usage Draytek Vigor 3900 CPU Usage
# TYPE draytek_vigor_3900_metric_cpu_usage gauge
draytek_vigor_3900_metric_cpu_usage{host="192.168.1.1"} 19
# HELP draytek_vigor_3900_metric_current_system_time Draytek Vigor 3900 Current System Time
# TYPE draytek_vigor_3900_metric_current_system_time gauge
draytek_vigor_3900_metric_current_system_time{host="192.168.1.1"} 28 Dec 2020 21:52:54 +0700
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
draytek_vigor_3900_metric_load_average1{host="192.168.1.1"} 1.71
# HELP draytek_vigor_3900_metric_load_average15 Draytek Vigor 3900 Load Average 15 Minutes
# TYPE draytek_vigor_3900_metric_load_average15 gauge
draytek_vigor_3900_metric_load_average15{host="192.168.1.1"} 1.02
# HELP draytek_vigor_3900_metric_load_average5 Draytek Vigor 3900 Load Average 5 Minutes
# TYPE draytek_vigor_3900_metric_load_average5 gauge
draytek_vigor_3900_metric_load_average5{host="192.168.1.1"} 1.28
# HELP draytek_vigor_3900_metric_memory_buffer Draytek Vigor 3900 Memory Buffer
# TYPE draytek_vigor_3900_metric_memory_buffer gauge
draytek_vigor_3900_metric_memory_buffer{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_cached Draytek Vigor 3900 Memory Cached
# TYPE draytek_vigor_3900_metric_memory_cached gauge
draytek_vigor_3900_metric_memory_cached{host="192.168.1.1"} 97416
# HELP draytek_vigor_3900_metric_memory_free Draytek Vigor 3900 Memory Free
# TYPE draytek_vigor_3900_metric_memory_free gauge
draytek_vigor_3900_metric_memory_free{host="192.168.1.1"} 49860
# HELP draytek_vigor_3900_metric_memory_process_top_1 Draytek Vigor 3900 memory process top 1
# TYPE draytek_vigor_3900_metric_memory_process_top_1 gauge
draytek_vigor_3900_metric_memory_process_top_1{host="192.168.1.1"} 0.3
# HELP draytek_vigor_3900_metric_memory_process_top_10 Draytek Vigor 3900 memmory process top 10
# TYPE draytek_vigor_3900_metric_memory_process_top_10 gauge
draytek_vigor_3900_metric_memory_process_top_10{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_process_top_2 Draytek Vigor 3900 memmory process top 2
# TYPE draytek_vigor_3900_metric_memory_process_top_2 gauge
draytek_vigor_3900_metric_memory_process_top_2{host="192.168.1.1"} 0.2
# HELP draytek_vigor_3900_metric_memory_process_top_3 Draytek Vigor 3900 memory process top 3
# TYPE draytek_vigor_3900_metric_memory_process_top_3 gauge
draytek_vigor_3900_metric_memory_process_top_3{host="192.168.1.1"} 4.1
# HELP draytek_vigor_3900_metric_memory_process_top_4 Draytek Vigor 3900 memmory process top 4
# TYPE draytek_vigor_3900_metric_memory_process_top_4 gauge
draytek_vigor_3900_metric_memory_process_top_4{host="192.168.1.1"} 2.4
# HELP draytek_vigor_3900_metric_memory_process_top_5 Draytek Vigor 3900 memory process top 5
# TYPE draytek_vigor_3900_metric_memory_process_top_5 gauge
draytek_vigor_3900_metric_memory_process_top_5{host="192.168.1.1"} 2.3
# HELP draytek_vigor_3900_metric_memory_process_top_6 Draytek Vigor 3900 memmory process top 6
# TYPE draytek_vigor_3900_metric_memory_process_top_6 gauge
draytek_vigor_3900_metric_memory_process_top_6{host="192.168.1.1"} 1.8
# HELP draytek_vigor_3900_metric_memory_process_top_7 Draytek Vigor 3900 memory process top 7
# TYPE draytek_vigor_3900_metric_memory_process_top_7 gauge
draytek_vigor_3900_metric_memory_process_top_7{host="192.168.1.1"} 1.1
# HELP draytek_vigor_3900_metric_memory_process_top_8 Draytek Vigor 3900 memmory process top 8
# TYPE draytek_vigor_3900_metric_memory_process_top_8 gauge
draytek_vigor_3900_metric_memory_process_top_8{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_process_top_9 Draytek Vigor 3900 memory process top 9
# TYPE draytek_vigor_3900_metric_memory_process_top_9 gauge
draytek_vigor_3900_metric_memory_process_top_9{host="192.168.1.1"} 0.9
# HELP draytek_vigor_3900_metric_memory_shards Draytek Vigor 3900 Memory Shards
# TYPE draytek_vigor_3900_metric_memory_shards gauge
draytek_vigor_3900_metric_memory_shards{host="192.168.1.1"} 0
# HELP draytek_vigor_3900_metric_memory_used Draytek Vigor 3900 Memory Used
# TYPE draytek_vigor_3900_metric_memory_used gauge
draytek_vigor_3900_metric_memory_used{host="192.168.1.1"} 172036
# HELP draytek_vigor_3900_metric_model Draytek Vigor 3900 Model
# TYPE draytek_vigor_3900_metric_model gauge
draytek_vigor_3900_metric_model{host="192.168.1.1"} 3900
# HELP draytek_vigor_3900_metric_revision Draytek Vigor 3900 revision
# TYPE draytek_vigor_3900_metric_revision gauge
draytek_vigor_3900_metric_revision{host="192.168.1.1"} 8172
# HELP draytek_vigor_3900_metric_system_up_time Draytek Vigor 3900 system up time
# TYPE draytek_vigor_3900_metric_system_up_time gauge
draytek_vigor_3900_metric_system_up_time{host="192.168.1.1"} 109 days 15 hours 39 minutes 16 seconds
```
