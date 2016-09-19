from netmiko import ConnectHandler

conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.70', username='pyclass', password='88newclass')

conn.send_command('config t')
conn.send_config_from_file('config.txt')
conn.send_command('exit')


conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.70', username='pyclass', password='88newclass')
output = conn.send_command('show run')
print output

