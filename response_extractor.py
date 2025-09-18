import json

def main(response_info) -> dict:
    if isinstance(response_info, str):
        data = json.loads(response_info)
    else:
        data = response_info

    requisitionNumber = str(data["requisiontionNumber"])
    msg = data['msg']
    if msg is None:
        msg = ""
    else:
        msg = str(msg)

    return {
        "requisitionNumber": requisitionNumber,
        "msg": msg
    }