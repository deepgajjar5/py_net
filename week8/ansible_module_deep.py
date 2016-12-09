from ansible.module_utils.basic import AnsibleModule 
import pyeapi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from jsonrpclib import Server



#class VlanAnsibleModule(AnsibleModule):
        
def main():
  
    argument_spec = dict( 
        vlan_id=dict(required=True), 
        vlan_name=dict(),
        host=dict(),
        username=dict(required=True),
        password=dict(required=True), 
        port=dict(required=False),
        transport=dict(choices=['http', 'https'],required=False)
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    
    vlan_id = module.params['vlan_id']
    vlan_name = module.params['vlan_name']
    host = str(module.params['host'])
    username = module.params['username']
    password = module.params['password']
    port = int(module.params['port'])
    transport = module.params['transport']

    conn = Server("https://%s:%s@%s/command-api" %(username, password, host))
    
    list_cmds = [ "enable", "configure" ] 

    list_cmds.append("vlan %s" %(vlan_id))
    list_cmds.append("name %s" %(vlan_name))

    conn.runCmds(1, list_cmds, "json")

    module.exit_json(msg="Vlan created successfully")

if __name__ == "__main__":
    main()
