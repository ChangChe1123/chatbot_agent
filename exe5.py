import requests
url = 'test'

def main(description, placeName, unitName, travel_description):
    expInfoLines = []
    for i in range(len(placeName)):
        if travel_description[i]:
            line_description = travel_description[i]
        else:
            line_description = description

        expInfoLines.append({
            'placeName': placeName,
            'unitName': unitName,
            'description': line_description
        })

    data = {
        'description': description,
        'expInfoLines': expInfoLines
    }

    try:
        resp = requests.post(url, json=data)

        try:
            response_info = resp.json()
        except ValueError:
            response_info = {"raw_response" : resp.text}

        return {
            'status_code': resp.status_code,
            'response_header': dict(resp.headers),
            'response_info': response_info,
            'data_object': data
        }
    except requests.exceptions.RequestException as e:
        return {
            'error': str(e)
        }