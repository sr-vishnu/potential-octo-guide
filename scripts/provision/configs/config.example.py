import json
import pathlib

def _retrive_ssh_key(path):
    with open(path,'r') as fp:
        key = json.load(fp).get("public-key")
    return key
    
config = {
    "zone_name":"",
    "region_name":"",
    "project_name":"",
    "network_name":"",
    "subnet_name":"",
    "nat_name":"",
    "vm_ssh_key": _retrive_ssh_key(pathlib.Path(__file__).parent.parent/"secrets"/"ssh-keys"/"public-key.json"),
    "router_name":"",
    "service_account":""
}