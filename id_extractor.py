"""
http input:
{
    "approvers": ["cc"]
}
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

"""
处理后要得到的是:
{
“result": {
            "cc": [
                    { 
                        "fdNo":"123",
                        "fdDept":"abc"
                    },
                    {
                        "fdNo":"124",
                        "fdDept":"abc"
                    }
                 ]
           }
}               
"""
import requests

url = "test"

def main(approvers) -> dict:
    data = {
        "fdNames" : approvers
    }
    headers = {}
    resp = requests.post(url, json=data, headers=headers)

    result = preprocess(resp.json())
    output = text_output(result)
    #所有审批人都有唯一id的时候，方便直接调用API
    if '多个' not in output:
        ids = []
        for approver in approvers:
            if approver in result and len(result[approver]) == 1:
                ids.append(result[approver][0]['fdNo'])
            else:
                ids.append('')
    else:
        ids = ['']

    return {
        "result": result,
        "text_output": output,
        "ids": ids
    }

# 输入给大模型的文本
def text_output(result):
    output = ""
    for name, records in result.items():
        if len(records) == 1:
            output += f"审批人[{name}]有唯一工号{records[0]['fdNo']}，部门是{records[0]['fdDept']}。\n"
        else:
            details = []
            for i, record in enumerate(records, start=1):
                details.append(f"{i}. 工号{record['fdNo']}，部门{record['fdDept']}")
            details_str = "\n   ".join(details)
            output += f"审批人[{name}]有多个工号和部门，分别是：\n   {details_str}\n"
    return output

# json.loads(), resp.json()都是返回字典
def preprocess(json_input):
    data = json_input["data"] #json_input这个字典中，key=data这一项，得到一个列表
    result = {} #定义一个空字典
    for item in data:    #遍历data这个列表，列表中每个item也是个字典
        name = item["fdName"]
        fdNo = item["fdNo"]
        fdDept = item["fdDept"]
        if(name not in result): # 如果key ="cc"不在result这个字典中
            result[name] = []   # 创建一个key = "cc"的空列表
        result[name].append({"fdNo": fdNo, "fdDept": fdDept})
    return result

