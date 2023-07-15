import pdpyras
import requests
import json

# API_KEY = << USER API Key >>'

headers = {
    'Accept': 'application/vnd.pagerduty+json;version=2',
    'Authorization': 'Token token=<< USER API Key >>',
    'Content-Type': 'application/json',
}

response = requests.get('https://api.pagerduty.com/incidents?limit=1000&statuses[]=triggered&user_ids[]=P9I9UAO', headers=headers)

json_object = response.json()
incidents = json_object["incidents"]

if  len(incidents) == 0:
    print("No new Incident Triggered.")
    exit

json_data = {
    'incident': {
        'type': 'incident',
        'status': 'acknowledged',
    },
}

for incident in incidents:
    incident_id = incident["id"]
    incident_title = incident["title"]
    response = requests.put('https://api.pagerduty.com/incidents/' + incident_id + '', headers=headers, json=json_data)
    print(incident_id, incident_title, " -> ", response)
