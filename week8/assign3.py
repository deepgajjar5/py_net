from net_system.models import NetworkDevice

pynet_sw5 = NetworkDevice.objects.get_or_create(
    device_name='pynet_sw5',
    device_type='arista_eos',
    ip_address='99.99.99.99',
    port=324,
)

pynet_sw6 = NetworkDevice.objects.get_or_create(
    device_name='pynet_sw6',
    device_type='arista_eos',
    ip_address='99.99.99.98',
    port=325,
)

