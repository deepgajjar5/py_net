from netmiko import ConnectHandler

conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.71', username='pyclass', password='88newclass')

conn.send_command('config t')
conn.send_command('logging buffered 28280')
conn.send_command('exit')
output = conn.send_command('show run')

print output
