import requests

PROXMOX_URL = "https://YOUR_PROXMOX_IP:8006/api2/json"
NODE = "pve"
TOKEN_ID = "USER@pam!SOMENAME"
TOKEN_SECRET = "API-KEY"

headers = {
    "Authorization": f"PVEAPIToken={TOKEN_ID}={TOKEN_SECRET}"
}

# Disable SSL warnings (only for self-signed certificates)
requests.packages.urllib3.disable_warnings()

def get_nodes():
    response = requests.get(f"{PROXMOX_URL}/nodes", headers=headers, verify=False)
    if response.status_code == 200:
        nodes = response.json()['data']
        for node in nodes:
            print(node['node'])
    else:
        print(f"Error: {response.text}")

def get_vms():
    response = requests.get(f"{PROXMOX_URL}/nodes/{NODE}/qemu", headers=headers, verify=False)
    if response.status_code == 200:
        vms = response.json()['data']
        for vm in vms:
            print(f"VMID: {vm['vmid']}, Name: {vm.get('name', 'N/A')}, Status: {vm['status']}")
    else:
        print(f"Error: {response.text}")

def get_containers():
    response = requests.get(f"{PROXMOX_URL}/nodes/{NODE}/lxc", headers=headers, verify=False)
    if response.status_code == 200:
        containers = response.json()['data']
        for container in containers:
            print(f"CTID: {container['vmid']}, Name: {container.get('name', 'N/A')}, Status: {container['status']}")
    else:
        print(f"Error: {response.text}")

def get_storage():
    response = requests.get(f"{PROXMOX_URL}/nodes/{NODE}/storage", headers=headers, verify=False)
    if response.status_code == 200:
        storages = response.json()['data']
        for storage in storages:
            print(f"Storage ID: {storage['storage']}, Type: {storage['type']}, Used: {storage['used']}, Total: {storage['total']}, Free: {storage['avail']}")
    else:
        print(f"Error: {response.text}")

def list_isos(storage_name):
    response = requests.get(f"{PROXMOX_URL}/nodes/{NODE}/storage/{storage_name}/content", headers=headers, verify=False)
    if response.status_code == 200:
        contents = response.json()['data']
        for item in contents:
            if item['content'] == 'iso':
                print(item['volid'])
    else:
        print(f"Error fetching ISOs: {response.text}")



if __name__ == "__main__":
    get_nodes()
    get_vms()
    get_containers()
    get_storage()
    list_isos("local")  # Replace 'Media' with your storage name if different

