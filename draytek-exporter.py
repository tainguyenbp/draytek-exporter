from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException,NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from http.server import HTTPServer

import logging
import socket
import time
import threading
from prometheus.collectors import Gauge
from prometheus.registry import Registry
from prometheus.exporter import PrometheusMetricHandler
import psutil
import re

logging.basicConfig(filename="/var/log/draytek_exporter.log", level=logging.DEBUG)
#logging.getLogger('paramiko.transport').disabled = True

PORT_NUMBER = 9252

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

def draytek_gather_data(registry):
    host = '192.168.1.1'
    """Gathers the metrics"""

    # Get the host name of the machine

    metric_memory_usage = Gauge("draytek_vigor_3900_memory_usage", "Draytek Vigor 3900 Memory Usage", {'host': host})
    metric_cpu_usage = Gauge("draytek_vigor_3900_metric_cpu_usage", "Draytek Vigor 3900 CPU Usage", {'host': host})
    metric_memory_size = Gauge("draytek_vigor_3900_metric_memory_size", "Draytek Vigor 3900 Memory Size", {'host': host})
    metric_model = Gauge("draytek_vigor_3900_metric_model", "Draytek Vigor 3900 Model", {'host': host})
    metric_hardware_verison = Gauge("draytek_vigor_3900_metric_hardware_verison", "Draytek Vigor 3900 Hardware Version", {'host': host})
    metric_firmware_verison = Gauge("draytek_vigor_3900_metric_firmware_verison", "Draytek Vigor 3900 Firmware Version", {'host': host})
    metric_build_date_time = Gauge("draytek_vigor_3900_metric_build_date_time", "Draytek Vigor 3900 Build Date Time", {'host': host})
    metric_revision = Gauge("draytek_vigor_3900_metric_revision", "Draytek Vigor 3900 revision", {'host': host})
    metric_system_up_time = Gauge("draytek_vigor_3900_metric_system_up_time", "Draytek Vigor 3900 system up time", {'host': host})

    registry.register(metric_memory_usage)
    registry.register(metric_cpu_usage)
    registry.register(metric_model)
    registry.register(metric_hardware_verison)
    registry.register(metric_firmware_verison)
    registry.register(metric_build_date_time)
    registry.register(metric_revision)
    registry.register(metric_system_up_time)


    while True:
        time.sleep(1)
        mode_enable = 'enable'
  
        net_connect_device = ConnectHandler(**vigor_draytek_3900)
        net_connect_device.enable()
        
        command_show_status_system = 'status system'
       
        result_run_command = net_connect_device.send_command(mode_enable, expect_string=r'Entering enable mode...')
        result_run_command += net_connect_device.send_command(command_show_status_system, expect_string=r'#')
        
        [Model,Hardware_Version,Firmware_Version,Build_Date_Time,Revision,System_up_Time,CPU_usage,Memory_Size,Memory_Usage,Current_System_Time,EEPROM_Version,Bootloader_Version] = re.findall("\d.+", result_run_command)

        Memory_Usage = Memory_Usage[: len(Memory_Usage) - 1]
        CPU_usage = CPU_usage[: len(CPU_usage) - 1]
        
        metric_model.set({},Model)
        metric_hardware_verison.set({},Hardware_Version)
        metric_firmware_verison.set({},Firmware_Version)
        metric_build_date_time.set({},Build_Date_Time)
        metric_revision.set({},Revision)
        metric_system_up_time.set({},System_up_Time)
        metric_memory_usage.set({},Memory_Usage)
        metric_cpu_usage.set({},CPU_usage)
        metric_memory_size.set({},Memory_Size)

        net_connect_device.disconnect()

if __name__ == '__main__':
#    gather_data()
    # Create the registry
    registry = Registry()

    # Create the thread that gathers the data while we serve it
    thread = threading.Thread(target=draytek_gather_data, args=(registry, ))
    thread.start()

    # Set a server to export (expose to prometheus) the data (in a thread)
    try:
        # We make this to set the registry in the handler
        def handler(*args, **kwargs):
            PrometheusMetricHandler(registry, *args, **kwargs)

        server = HTTPServer(('', PORT_NUMBER), handler)
        server.serve_forever()

    except KeyboardInterrupt:
        server.socket.close()
        thread.join()

