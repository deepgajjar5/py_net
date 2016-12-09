from ansible.module_utils.basic import AnsibleModule 

def main():
    

    fields = { 
        "vlan_id": { "required": True, "type": "str" }, 
        "vlan_name": { "required": False, "type": "str"}, 
    }

    module = AnsibleModule(argument_spec=fields)
    print module.params

if __name__ == "__main__":
    main()
