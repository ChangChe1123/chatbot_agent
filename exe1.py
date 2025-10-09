import requests

""" 
http output:
{
    "success": true,
    "code" :"Success",
    "data": [
        {
         "fdNo":"123,
         "fdName": "cc",
         "fdDept": "abc
         },
         {
         "fdNo":"124,
         "fdName": "cb",
         "fdDept": "abc
         }
    ]
}
"""
def preprocess(json_input):
    data = json_input['data']  #list of dict
    result = {}
    for item in data:
        employee_name = data['employee_name']
        employee_id = data['employee_id']
        department = data['department']
        if employee_name not in result:
            result[employee_name] = []
            result[employee_name].append({
                'employee_id': employee_id,
                'department': department
            })
    return result

def text_output(result):
    output = ''
    for name, records in result.items():  # records is a list of dicts
        if len(records) == 1:
            output += f"{name}的唯一ID是{records[0]['employee_id']}，部门是{records[0]['department']}。\n"
        else:
            output += f"{name}有多个ID："
            for record in records:
                output += f"ID是{record['employee_id']}，部门是{record['department']}；"
            output = output.rstrip('；') + "。\n"
    return output

url = "test"
def main(approvers) -> dict:
    data = {
        'fdNames' : approvers
    }
    response = requests.post(url, json=data)
    result = preprocess(response.json())
    output = text_output(result)

    if '多个' not in output:
        ids = []
        for approver in approvers:
            if len(result[approver]) == 1:
                ids.append(result[approver][0]['employee_id'])
    else:
        ids = ['']

    return {
        'result': result,
        'text_output': output,
        'ids': ids
    }