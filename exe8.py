import json

'''
{
    "msg": "success",
    "data": [
        {
            "fdMeetingRoom": {
                "fdid": "abc",
                "fdName": "a大厦698会议室",
                "fdCategoryFullPathName": "a大厦"
            },
            "fdMeetings": [
                {
                    "fdid": "def",
                    "fdName": "xxx",
                    "fdStartTime": 1234,
                    "fdFinishTime": 5678,
                    "fdMeetingRoom":{
                        "fdid": "abc",
                        "fdStatus": "enable"
                    }
                }
            ]
        }
    ]
}
'''

def main(body_info, room_path, start_time, end_time) -> dict:
    data = json.loads(body_info)
    rooms_list = data["data"]
    result = []  # 原有的data中有太多冗余的信息，重新构建新的dict

    for item in rooms_list:
        room_info = item["fdMeetingRoom"]
        if room_info["fdCategoryFullPathName"] != room_path:
            continue
        meeting_lists = item.get("fdMeetings", [])
        new_fdMeetings = []
        for meeting in meeting_lists:
            new_meeting = {
                "fdid" : meeting["fdid"],
                "fdStartTime": meeting["fdStartTime"],
                "fdFinishTime": meeting["fdFinishTime"]
            }
            new_fdMeetings.append(new_meeting)
        extracted_data = {
            "fdid": room_info["fdid"],
            "fdName": room_info["fdName"],
            "fdCapacityNumber": room_info.get("fdCapacityNumber", "Missing"),
            "fdMeetings": new_fdMeetings
        }
        result.append(extracted_data)

    filtered_meeting_rooms = []
    for room in result:
        if check(start_time, end_time, room["fdMeetings"]):
            filtered_meeting_rooms.append(room)

    return {
        "filtered_rooms": filtered_meeting_rooms,
        "total_size": len(filtered_meeting_rooms)
    }



def check(start_time, end_time, fdMeetings):
    if len(fdMeetings) == 0:
        return True
    for meeting in fdMeetings:
        meeting_start = meeting["fdStartTime"]
        meeting_end = meeting["fdFinishTime"]
        if start_time < meeting_end or end_time > meeting_start:
            return False
    return True
