import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# load API token from enviroment
token = os.getenv('TOKEN')

print("Creates FRONT ports from REAR ports and copies the attributes")

# Ask user for input until correct device was chosen
device_chosen = False
while device_chosen == False:
  device_id = input("Device ID:")

  headers = {
    'Authorization': "Token "+token,
    'Content-Type': "application/json"
  }

  params = {'device_id': device_id}
  response = requests.get('https://netbox.brienznet.ch/api/dcim/rear-ports', headers=headers, params=params)
  rear_ports = response.json()
  rear_ports = rear_ports['results']
  device_name = rear_ports[0]['device']['display']
  correct_device_answer = input("Is this the correct device? "+device_name+": [y/N] ")

  # Ask user to check the chosen device
  if correct_device_answer == "y" or correct_device_answer == "Y":
    device_chosen = True
  else:
    print("Reseting... wrong device entered...")


# Set labels of the front ports based on the label from the corresponding rear port
for p in rear_ports:
  print("Port ID:", p["id"])
  print("Port Label:", p["label"])
  # print("Front Port ID:", p["front_port"]["id"])
  print("-----------")

  data = {
    "device": p["device"]["id"],
    "module": p['module'],
    "name": p['name'],
    "label": p['label'],
    "type": p['type']['value'],
    "color": p['color'],
    "rear_port": p['id'],
    "rear_port_position": 1,
    "description": p['description'],
    "mark_connected": p['mark_connected']
  }

  front_port = requests.post('https://netbox.brienznet.ch/api/dcim/front-ports/', headers=headers, data=json.dumps(data))
  front_port = front_port.json()

  print(front_port)

  # print(front_port)
  print("---------------------")