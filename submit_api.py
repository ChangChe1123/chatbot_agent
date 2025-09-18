"""
http request
{
    "requisitionNumber": "REQ9082,
    "approver_id": [
        {
            "sequence": 1,
            "userCode": "88000134"
        },
        {
            "sequence": 2,
            "userCode": "88000135"
        }
    ]
"""
import requests

url = "test"

def main(requisitionNumber, approver_ids):
    yc_options = []
    for sequence, user_code in enumerate(approver_ids, start=1):
        yc_options.append({
            "sequence": sequence,
            "userCode": user_code
        })
    data = {
        "requisitionNumber": requisitionNumber,
        "approver_id": yc_options
    }
    headers = {}
    resp = requests.post(url, json=data, headers=headers)
    return {
        "status_code": resp.status_code,
        "response_info": resp.json(),
        "data_object": data
    }