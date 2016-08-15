from snmp_helper import snmp_get_oid, snmp_extract

community_string = "galileo"

port = 161

ip_addr = "184.105.247.70"

snmp_connection = (ip_addr, community_string, port)

snmp_data = snmp_get_oid(snmp_connection, oid="1.3.6.1.2.1.1.1.0", display_errors=True)

sysDesc = snmp_extract(snmp_data)

snmp_data = snmp_get_oid(snmp_connection, oid="1.3.6.1.2.1.1.5.0", display_errors=True)

sysName = snmp_extract(snmp_data)

print sysDesc

print sysName
