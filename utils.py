# utils.py
def handle_response_errors(response):
    if response['status_code'] != 200:
        raise Exception(f"Error: {response['error_message']}")
    return response['data']
