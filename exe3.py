import re
from datetime import datetime

def extract_travel_info(text, time_format):
    travel_info = {
        'departureDate': None,
        'placeName': None
    }

    try:
        departure_time_match = re.search(r'出发时间:\s*"([^"]+)")', text)
        if departure_time_match:
            departure_time = departure_time_match.group(1)
            travel_info['departureDate'] = datetime.strptime(departure_time, time_format)

        place_match = re.search(r'出发地:\s*"([^"]+)"', text)
        if place_match:
            travel_info['placeName'] = place_match.group(1).split(' 、')

    except ValueError as e:
        print(f"error{e}")
        return travel_info