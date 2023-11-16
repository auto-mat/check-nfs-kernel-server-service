#!/usr/bin/env python3

"""
Check if aloting IP address is assigned to the droplet, if not reassign
it.
"""

import json
import os
import requests
import sys

FLOATING_IP_ADDRESS = os.getenv("DO_FLOATING_IP_ADDRESS")
BASE_URL = os.getenv("DO_BASE_API_URL")
LIST_ALL_FLOATING_IPS_URL = f"{BASE_URL}/floating_ips"
LIST_ALL_DROPLETS_URL = f"{BASE_URL}/droplets"
ASSIGN_FLOATING_IP_TO_DROPLET_URL = (
    f"{BASE_URL}/floating_ips/{FLOATING_IP_ADDRESS}/actions"
)

HEADERS = {
    "Authorization": f"Bearer {os.getenv('DO_KUBERNETES_TOKEN')}",
}


def is_floating_ip_address_assigned():
    """Check if floating IP address is assigned into droplet

    :return None|dict: None if floating IP address is not assigned into
                       droplet elsa droplet dict info
    """
    response = requests.get(
        LIST_ALL_FLOATING_IPS_URL,
        headers=HEADERS,
    )
    code = response.status_code
    if code != 200:
        sys.exit(
            "Error getting list all of floating IPs addresses info,"
            " status code {code}."
        )
    for i in response.json()["floating_ips"]:
        if i["ip"] == FLOATING_IP_ADDRESS:
            return i["droplet"]


def list_all_of_droplets():
    """List all of droplets

    :return list: list of all droplets id
    """
    droplets = []
    response = requests.get(
        LIST_ALL_DROPLETS_URL,
        headers=HEADERS,
    )
    code = response.status_code
    if code != 200:
        sys.exit("Error getting list all of droplets, status code {code}.")
    for i in response.json()["droplets"]:
        droplets.append(i["id"])
    return droplets


def assign_floating_ip_address(droplet_id):
    """Assign floating IP address into droplet

    :param int droplet_id: droplet id which it will be assigned floating
                           IP address

    :return None
    """
    data = {
        "type": "assign",
        "droplet_id": droplet_id,
    }
    response = requests.post(
        ASSIGN_FLOATING_IP_TO_DROPLET_URL,
        headers=HEADERS,
        data=json.dumps(data),
    )
    code = response.status_code
    if code != 201:
        sys.exit(
            f"Error assign IP address {FLOATING_IP_ADDRESS} to the droplet id"
            f" {droplet_id}, status code {code}."
        )
    print(f"Assign IP address {FLOATING_IP_ADDRESS} to the droplet id {droplet_id}.")


def main():
    assigned = is_floating_ip_address_assigned()
    if not assigned:
        droplets_id = list_all_of_droplets()
        assign_floating_ip_address(droplet_id=droplets_id[0])
    else:
        print(
            f"Floating IP address {FLOATING_IP_ADDRESS} is assigned to"
            f" the droplet id {assigned['id']}, name {assigned['name']}."
        )


if __name__ == "__main__":
    main()
