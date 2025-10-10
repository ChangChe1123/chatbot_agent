def main(approver_id):
    options = []
    for sequence, user_code in enumerate(approver_id, start=1):
        options.append({
            'sequence': sequence,
            'userCode': user_code
        })

    data = {
        'options': options
    }