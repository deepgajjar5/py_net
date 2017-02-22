from net_system.models import NetworkDevice, Credentials
import django
django.setup()
from netmiko import ConnectHandler
import timeit 
import threading 

devices = NetworkDevice.objects.all()

creds = Credentials.objects.all()

dict_of_ip = {}
dict_of_hostname = {}

uname = ""
device_name = ""

for device_list in devices:
    uname =  getattr(device_list, 'credentials')
    device_name = getattr(device_list, 'device_name')
    ip = getattr(device_list, 'ip_address')
    device_type = getattr(device_list, 'device_type')

    dict_of_ip[ip] = uname
    dict_of_hostname[uname] = device_name 
    #print ip

# Contains mapping of Hostnames to Usernames

dict_of_username = {}

username = ""
passowrd = ""

for cred in creds:
    
    username = getattr(cred, 'username')
    password = getattr(cred, 'password')  

 
    dict_of_username[username] = password

# Contains mapping of Username to Passwords

password = ""
username = ""
platform = ""
ip = ""

start = timeit.default_timer()

for key, value in dict_of_ip.iteritems():
    if str(value) in dict_of_username:
        password = dict_of_username[str(value)]

        hostname = dict_of_hostname[value]

        ip = str(key)
        
        if hostname.startswith('pynet-rtr'):
            platform = "cisco_ios"

        elif hostname.startswith('pynet-sw'):
            platform = "arista_eos"

        else:
            platform = "juniper"

        username = str(value)

        device = ConnectHandler(device_type=platform, ip=ip, username=username, password=password)

        output = device.send_command("show version")

        print output         

stop = timeit.default_timer()

print stop - start 

