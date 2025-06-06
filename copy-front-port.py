import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# load API token from enviroment
token = os.getenv('TOKEN')

print("Copy FRONT ports to REAR ports")

# Ask user for input until correct device was chosen
device_chosen = False
while device_chosen == False:
  device_id = input("Device ID:")

  headers = {
    'Authorization': "Token "+token,
    'Content-Type': "application/json"
  }

  params = {'device_id': device_id}
  response = requests.get('https://netbox.brienznet.ch/api/dcim/front-ports', headers=headers, params=params)
  front_ports = response.json()
  front_ports = front_ports['results']
  device_name = front_ports[0]['device']['display']
  correct_device_answer = input("Is this the correct device? "+device_name+": [y/N] ")

  # Ask user to check the chosen device
  if correct_device_answer == "y" or correct_device_answer == "Y":
    device_chosen = True
  else:
    print("Reseting... wrong device entered...")


# Set labels of the rear ports based on the label from the corresponding front port
for p in front_ports:
  print("Port ID:", p["id"])
  print("Port Label:", p["label"])
  print("Rear Port ID:", p["rear_port"]["id"])
  print("-----------")

  data = {
    'label': p["label"]
  }

  rear_port = requests.patch('https://netbox.brienznet.ch/api/dcim/rear-ports/'+str(p["rear_port"]["id"])+"/", headers=headers, data=json.dumps(data))
  rear_port = rear_port.json()

  print(rear_port)
  print("---------------------")