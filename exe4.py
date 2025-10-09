import requests

url = 'test'

def main(placeName, unitName, travel_description, description):
    request_lines = []
    for i in range(len(placeName)):
        if travel_description[i]:
            line_description = travel_description[i]
        else:
            line_description = description

        request_lines.append({
            'placeName': placeName[i],
            'unitName': unitName[i],
            'description': line_description
        })

    data = {
        'lines': request_lines
    }

    response = requests.post(url, json=data)
    return response.json()