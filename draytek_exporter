from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException,NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from http.server import HTTPServer

import socket
import time
import threading
from prometheus.collectors import Gauge
from prometheus.registry import Registry
from prometheus.exporter import PrometheusMetricHandler
import psutil
import re

PORT_NUMBER = 9250

cisco_ios = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,
    'secret': 'admin',
}

def gather_data(registry):
#def gather_data():
    """Gathers the metrics"""
    host = '192.168.1.1'
    stacks_1 = 'stacks 1'
    stacks_2 = 'stacks 2'
    # Get the host name of the machine

    metric_total_disk_stacks1 = Gauge("cisco_switch_3650_total_disk_stacks1_bytes", "Cisco switch 3650 total disk stacks 1", {'host': host, 'stacks': stacks_1})
    metric_free_disk_stacks1 = Gauge("cisco_switch_3650_free_disk_stacks1_bytes", "Cisco switch 3650 free disk stacks 1", {'host': host, 'stacks': stacks_1})
    metric_used_disk_stacks1 = Gauge("cisco_switch_3650_used_disk_stacks1_bytes", "Cisco switch 3650 used disk of stacks 1", {'host': host, 'stacks': stacks_1})
    metric_total_disk_stacks2 = Gauge("cisco_switch_3650_total_disk_stacks2_bytes", "Cisco switch 3650 total disk stacks 2", {'host': host, 'stacks': stacks_2})
    metric_free_disk_stacks2 = Gauge("cisco_switch_3650_free_disk_stacks2_bytes", "Cisco switch 3650 free disk stacks 2", {'host': host, 'stacks': stacks_2})
    metric_used_disk_stacks2 = Gauge("cisco_switch_3650_used_disk_stacks2_bytes", "Cisco switch 3650 used disk of stacks 2", {'host': host, 'stacks': stacks_2})
    
    registry.register(metric_total_disk_stacks1)
    registry.register(metric_free_disk_stacks1)
    registry.register(metric_used_disk_stacks1)
    registry.register(metric_total_disk_stacks2)
    registry.register(metric_free_disk_stacks2)
    registry.register(metric_used_disk_stacks2)

    
    net_connect = ConnectHandler(**cisco_ios)
    while True:
        time.sleep(1)

        command_show_infor_disk_stacks1 = 'dir flash-1:/ | include bytes | include total | include free'
        command_show_infor_disk_stacks2 = 'dir flash-2:/ | include bytes | include total | include free'        
        
        result_run_command_show_infor_disk_stacks1 = net_connect.send_command(command_show_infor_disk_stacks1)
        result_run_command_show_infor_disk_stacks2 = net_connect.send_command(command_show_infor_disk_stacks2)
    
        [value_total_disk_stacks1,value_free_disk_stacks1] = re.findall("\d+", result_run_command_show_infor_disk_stacks1)
        [value_total_disk_stacks2,value_free_disk_stacks2] = re.findall("\d+", result_run_command_show_infor_disk_stacks2)

        value_used_disk_stacks1 = int(value_total_disk_stacks1) - int(value_free_disk_stacks1)
        value_used_disk_stacks2 = int(value_total_disk_stacks2) - int(value_free_disk_stacks2)
    
        metric_free_disk_stacks1.set({},value_free_disk_stacks1)
        metric_used_disk_stacks1.set({},value_used_disk_stacks1)
        metric_total_disk_stacks1.set({},value_total_disk_stacks1)
        metric_free_disk_stacks2.set({},value_free_disk_stacks2)
        metric_used_disk_stacks2.set({},value_used_disk_stacks2)
        metric_total_disk_stacks2.set({},value_total_disk_stacks2)


#    print('total disk: ',metric_total_disk_stacks1)
#    print('free disk: ',metric_free_disk_stacks1)
#    print('used disk: ',metric_used_disk_stacks1)

#    print('total disk: ',metric_total_disk_stacks2)
#    print('free disk: ',metric_free_disk_stacks2)
#    print('used disk: ',metric_used_disk_stacks2)

if __name__ == '__main__':
#    gather_data()
    # Create the registry
    registry = Registry()

    # Create the thread that gathers the data while we serve it
    thread = threading.Thread(target=gather_data, args=(registry, ))
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

