import json

'''
input:
{
    'response_info': {
        'expRequisitionNumber': 'REQ8000202510010',
        'expRequisitionHeaderId': 8306,
        'msg': null
    }
}
output:
{
    'expRequisitionNumber': 'REQ8000202510010',
    'expRequisitionHeaderId': 8306,
    'msg': ''
}
'''

def main(response_info) -> dict:
    if isinstance(response_info, str):
        data = json.loads(response_info)  #解析字符串为字典
    else:
        data = response_info

    expRequisitionNumber = str(data['expRequisitionNumber'])
    expRequisitionHeaderId = str(data['expRequisitionHeaderId'])

    msg = data['msg']
    if msg is None:
        msg = ''
    else:
        msg = str(msg)

    return {
        'expRequisitionNumber': expRequisitionNumber,
        'expRequisitionHeaderId': expRequisitionHeaderId,
        'msg': msg
    }