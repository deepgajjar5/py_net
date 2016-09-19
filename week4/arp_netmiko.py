from netmiko import ConnectHandler

conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.71', username='pyclass', password='88newclass')

output = conn.send_command('show arp')
print output


conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.70', username='pyclass', password='88newclass')
output = conn.send_command('show arp')
print output


conn = ConnectHandler(device_type='juniper', ip='184.105.247.76', username='pyclass', password='88newclass')
output = conn.send_command('show arp')
print output

