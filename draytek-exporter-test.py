from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException,NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from http.server import HTTPServer
import re
import requests
from netmiko import ConnectHandler
import logging
from datetime import datetime, timedelta
from netmiko.ssh_exception import NetMikoTimeoutException,NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException


logging.basicConfig(filename="/home/tainn/draytek_exporter/draytek_exporter.log", level=logging.DEBUG)


vigor_draytek_3900 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
}
mode_enable = 'enable'
  
net_connect_device = ConnectHandler(**vigor_draytek_3900)
net_connect_device.enable()
        
command_show_system = 'status system'
command_show_process = 'status process'

result_run_command_system = ''
result_run_command_process = ''
   
result_run_command = net_connect_device.send_command(mode_enable, expect_string=r'Entering enable mode...')

result_run_command_system += net_connect_device.send_command(command_show_system, expect_string=r'#')
#print(result_run_command_system)
[Model,Hardware_Version,Firmware_Version,Build_Date_Time,Revision,System_up_Time,CPU_usage,Memory_Size,Memory_Usage,Current_System_Time,EEPROM_Version,Bootloader_Version] = re.findall("\d.+", result_run_command_system)

result_run_command_process += net_connect_device.send_command(command_show_process, expect_string=r'#')
#print(result_run_command_process)
process = re.findall("\d.+", result_run_command_process)

print("Memory: "+ process[0])
print("Load Average: "+  process[1])
#

#print("CPU usage: "+ CPU_usage)

net_connect_device.disconnect()