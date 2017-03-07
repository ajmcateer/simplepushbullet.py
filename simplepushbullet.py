"""A simple Pushbullet interface"""
import requests

def send_message(title, message, api_key):
    """Sends text note to pushbullet notification"""

    url = "https://api.pushbullet.com/v2/pushes"
    payload = "{\"body\":\""+ message + "\",\"title\":\""+ title +"\",\"type\":\"note\"}\r\n"
    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text

def send_list(title, message, api_key):
    """Send notification"""
    message_str = "\n".join(message)

    url = "https://api.pushbullet.com/v2/pushes"
    payload = "{\"body\":\""+ repr(message_str)+"\",\"title\":\""+ title +"\",\"type\":\"note\"}\r\n"
    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text

def get_pushes(api_key):
    #if limit > 500:
     #   limit = 500

    url = "https://api.pushbullet.com/v2/pushes"

    headers = {
        'access-token': "o.vcqOkijhQRNJ5XjRxECXaTRbdm4dlQIg",
        'content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers)

    return response.text

def delete_push(api_key, iden):
    url = "https://api.pushbullet.com/v2/pushes/" + iden

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("DELETE", url, headers=headers)

    return response.text

def delete_all_pushed(api_key):
    url = "https://api.pushbullet.com/v2/pushes/"

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("DELETE", url, headers=headers)

    return response.text

def get_all_devices:
    url = "https://api.pushbullet.com/v2/devices"

    headers = {
        'access-token': "o.vcqOkijhQRNJ5XjRxECXaTRbdm4dlQIg",
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)

    return response.text

get_pushes("o.vcqOkijhQRNJ5XjRxECXaTRbdm4dlQIg")
