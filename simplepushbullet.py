"""A simple Pushbullet interface"""
import requests

def send_message(title, message, api_key):
    """Sends text note to pushbullet notification"""

    url = "https://api.pushbullet.com/v2/pushes"
    payload = "{\"body\":\""+ message + "\",\"title\":\""+ title +"\",\"type\":\"note\"}\r\n"
    headers = {
        'access-token': api_key,
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "30fcf100-2b7b-8707-1de7-6014da51140b"
        }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text

def send_list(title, message, api_key, divider):
    """Send notification"""

    messagestr = divider.join(message)

    url = "https://api.pushbullet.com/v2/pushes"
    payload = "{\"body\":\""+ messagestr + "\",\"title\":\""+ title +"\",\"type\":\"note\"}\r\n"
    headers = {
        'access-token': api_key,
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "30fcf100-2b7b-8707-1de7-6014da51140b"
        }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text
