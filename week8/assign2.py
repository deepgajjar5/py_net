from net_system.models import NetworkDevice, Credentials
devices = NetworkDevice.objects.all()

#for device in devices:
#    if "pynet-rtr" in device.device_name:
#        device.vendor = 'Cisco'
#    elif "pynet-sw" in device.device_name:
#        device.vendor = 'Arista'
#    else:
#        device.vendor = 'Juniper'
#
#    device.save()

for device in devices:
    print device.device_name, device.vendor
