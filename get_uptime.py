import requests
import json


url = 'http://127.0.0.1:8080/ins'
switchuser = 'vagrant'
switchpassword = 'vagrant'

headers = {'content-type': 'application/json-rpc'}
payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show version",
            "version": 1
        },
        "id": 1
    }
]

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(switchuser, switchpassword)).json()

for k, v in response['result'].items():
    print('{}, {}; has been up for {} days, {} hours, {} minutes, and {} seconds.'
          .format(v['host_name'],
                  v['chassis_id'],
                  v['kern_uptm_days'],
                  v['kern_uptm_hrs'],
                  v['kern_uptm_mins'],
                  v['kern_uptm_secs']))
