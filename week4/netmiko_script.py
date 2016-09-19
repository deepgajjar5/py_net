from netmiko import ConnectHandler

conn = ConnectHandler(device_type='cisco_ios', ip='184.105.247.71', username='pyclass', password='88newclass')

conn.send_command('config t')
print conn.find_prompt()
