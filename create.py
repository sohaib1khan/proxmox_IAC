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

def create_vm():
    # Define VM Configuration
    vm_config = {
        "vmid": 222,
        "name": "NewVM",
        "ostype": "l26",
        "memory": 2048,
        "net0": "virtio,bridge=vmbr0",
        "description": "Created via API",
        "ide2": "local:iso/AlmaLinux-8-latest-x86_64-boot.iso,media=cdrom",
        "virtio0": "S1:10,cache=none",  # This line creates a 10GB disk on the S1 storage
        "bootdisk": "virtio0",
        "boot": "dc"
    }


    # Create VM
    response = requests.post(f"{PROXMOX_URL}/nodes/{NODE}/qemu", data=vm_config, headers=headers, verify=False)
    if response.status_code in [200, 201]:
        print(f"VM {vm_config['vmid']} created successfully!")
        
        # Start VM
        start_vm(vm_config['vmid'])
    else:
        print(f"Error creating VM: {response.text}")

def start_vm(vmid):
    response = requests.post(f"{PROXMOX_URL}/nodes/{NODE}/qemu/{vmid}/status/start", headers=headers, verify=False)
    if response.status_code in [200, 201]:
        print(f"VM {vmid} started successfully!")
    else:
        print(f"Error starting VM {vmid}: {response.text}")

if __name__ == "__main__":
    create_vm()
