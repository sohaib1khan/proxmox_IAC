#  Proxmox Virtual Environment Automation

This repository contains Python scripts to interact with the Proxmox API, allowing users to manage and automate VM lifecycle tasks within a Proxmox environment. With these scripts, you can create, start, stop, delete, and list VMs, nodes, and storage details.

## Prerequisites

1. Python 3.x

2. `requests` library: Install via `pip install requests`

3. Proxmox environment with API access.

##  Setup

1. Clone this repository:

```bash

git clone [YOUR_REPOSITORY_URL]

cd proxmox_iac

Update the following variables in each script (`delete_vm.py`, `list_nodes.py`, `create.py`) to match your Proxmox environment:

```
PROXMOX_URL = "YOUR_PROXMOX_URL"
NODE = "YOUR_NODE_NAME"
TOKEN_ID = "YOUR_TOKEN_ID"
TOKEN_SECRET = "YOUR_TOKEN_SECRET"
```

## Scripts

### 1. `delete_vm.py`

This script allows you to list all the VMs in your Proxmox environment and select a VM to delete.

Usage:

```
python3 delete_vm.py
```

### `list_nodes.py`

This script lists details of nodes, VMs, containers, storage, and ISO files in your Proxmox environment.

Usage:

```
python3 list_nodes.py
```

### `create.py`

This script automates the creation and starting of a VM in your Proxmox environment. It uses predefined configurations for the VM details.

Usage:

```
python3 create.py
```