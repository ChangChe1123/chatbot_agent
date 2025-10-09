from datetime import datetime

def is_time_gap_over_20s(time_str1, time_str2):
    try:
        format = "%Y-%m-%d %H:%M:%S"
        time1 = datetime.strptime(time_str1, format)
        time2 = datetime.strptime(time_str2, format)
        time_diff = abs((time2 - time1).total_seconds())
        return time_diff > 20
    except ValueError as e:
        print(f"Error parsing date/time: {e}")
        return False

def main(last_time, current_time) -> dict:
    return {
        'reset_intent': 'Yes' if is_time_gap_over_20s(last_time, current_time) else 'No'
    }