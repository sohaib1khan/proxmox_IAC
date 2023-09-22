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

def list_vms():
    vms = []
    response = requests.get(f"{PROXMOX_URL}/nodes/{NODE}/qemu", headers=headers, verify=False)
    if response.status_code == 200:
        for vm in response.json()['data']:
            vms.append((vm['vmid'], vm.get('name', 'N/A')))
    return vms

def delete_vm(vmid):
    response = requests.post(f"{PROXMOX_URL}/nodes/{NODE}/qemu/{vmid}/status/stop", headers=headers, verify=False)
    if response.status_code not in [200, 201]:
        print(f"Error stopping VM {vmid}: {response.text}")
        return

    # Give the VM a few seconds to stop
    import time
    time.sleep(5)

    response = requests.delete(f"{PROXMOX_URL}/nodes/{NODE}/qemu/{vmid}", headers=headers, verify=False)
    if response.status_code in [200, 201]:
        print(f"VM {vmid} deleted successfully!")
    else:
        print(f"Error deleting VM {vmid}: {response.text}")

if __name__ == "__main__":
    vms = list_vms()
    
    if not vms:
        print("No VMs found.")
        exit()

    print("List of VMs:")
    for index, (vmid, name) in enumerate(vms, start=1):
        print(f"{index}. VMID: {vmid}, Name: {name}")

    try:
        choice = int(input("Enter the number of the VM you want to delete: "))
        if 1 <= choice <= len(vms):
            vmid_to_delete = vms[choice-1][0]
            confirm = input(f"Are you sure you want to delete VM with VMID {vmid_to_delete}? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_vm(vmid_to_delete)
            else:
                print("Aborted!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")
