import pathlib
import random_name
from utils import read_text_file
from configs.config import config
from resources.subnet import SubNet
from resources.router import Router
from resources.network import Network
from resources.firewall import FireWall
from resources.instance import Instance


def create_networks():
    return {
        "networks": [str(Network(config))]
    }

def create_subnets():
    return {
        "networks": [str(SubNet(config))]
    }

def create_routers():
    return {
        "routers": [str(Router(config))]
    }

def create_firewall():
    results = {"firewalls": []}
    rule_names = ["allow-all-internal","allow-ssh-all"]
    for rule in rule_names:
        results["firewalls"].append(
            FireWall(
                config,
                {
                    "rule_name":rule
                }
            )
        )
    return results

def create_instances():
    results = {"instances":[]}
    HOST_FILE_PATH = (
        pathlib
        .Path(__file__)
        .absolute()
        .parent
        .parent
        .parent/"hosts.txt"
    )
    addresses = read_text_file(HOST_FILE_PATH)
    names = list(random_name.generate(len(addresses)))

    #creating the public instance
    public = {
        "instance_name": names.pop(),
        "ip": addresses.pop(),
        "is_public": True
    }
    public_instance = Instance(config,public)
    results["instances"].append(str(public_instance))

    #creating the rest of the instances
    for name , ip in zip(names,addresses):
        private = {
            "instance_name": name,
            "ip": ip,
            "is_public": False
        }
        results["instances"].append(str(Instance(config,private)))
    return results

def create_all():
    results = {}
    results.update(create_networks())
    results.update(create_subnets())
    results.update(create_firewall())
    results.update(create_routers())
    results.update(create_instances())
    return results



if __name__ == "__main__":
    results = create_all()
    print(results)