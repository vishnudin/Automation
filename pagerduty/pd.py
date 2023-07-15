import requests
import json

# API_KEY = '<< USER API KEY >>'

headers = {
    'Accept': 'application/vnd.pagerduty+json;version=2',
    'Authorization': 'Token token=<< USER API KEY >>',
    'Content-Type': 'application/json',
}

# response = requests.put('https://api.pagerduty.com/incidents/id', headers=headers, json=json_data)

json_data = {
    'incident': {
        'type': 'incident',
        'status': 'resolved',
    },
}

# response = requests.get('https://api.pagerduty.com/incidents/' + incident_id + '', headers=headers)

response = requests.get('https://api.pagerduty.com/incidents?limit=1000&statuses[]=triggered', headers=headers)

# response = requests.put('https://api.pagerduty.com/incidents/' + incident_id + '', headers=headers, json=json_data)

# print(response.json())
json_object = response.json()

# print(incidents["incidents"][0]["id"])

# json_object = json.loads(response.text)

for incident in json_object["incidents"]:
    incident_id = incident["id"]
    if incident["service"]["summary"] == "<< Summary name in incident >>s":
        response = requests.put('https://api.pagerduty.com/incidents/' + incident_id + '', headers=headers, json=json_data)
    print(incident_id, " -> ", response)
    

# print(response.text)

