import django 
django.setup()
from net_system.models import NetworkDevice, Credentials


new_device = NetworkDevice.objects.get(device_name='pynet_sw6')
#
#new_device.vendor = 'Arista'
#
#print new_device
#
#new_device.save()
#
new_device.delete()

devices = NetworkDevice.objects.all()

print devices

