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
    payload = "{\"body\":\"" + repr(message_str) + "\",\"title\":\"" + title + "\",\"type\":\"note\"}\r\n"
    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


def get_pushes(api_key, limit=500, active="true", modified_after=0):
    if limit > 500:
        limit = 500

    elif limit < 1:
        limit = 1

    url = "https://api.pushbullet.com/v2/pushes"

    payload = {'limit': limit, 'active': active, 'modified_after': modified_after}

    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }
    response = requests.request("GET", url, params=payload, headers=headers)

    return response.text


def dismiss_push(api_key, iden):
    url = "https://api.pushbullet.com/v2/pushes/" + iden

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("POST", url, headers=headers)

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


def get_all_devices(api_key):
    url = "https://api.pushbullet.com/v2/devices"

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)

    return response.text


def create_device(api_key,nickname="", model="", manufacturer="", app_version="", icon="desktop"):

    url = "https://api.pushbullet.com/v2/devices"

    # Can't get has_sms = true working hard coding to false till I figure it out leaving code to handle it though
    has_sms = "false"

    if has_sms == "true":
        payload = "{\"nickname\":\"" + nickname + "\",\"model\":\"" + model + "\",\"manufacturer\":\"" + manufacturer + "\"," \
              "\"app_version\":\"" + app_version + "\",\"icon\":\"" + icon + "\"}"
    else:
        payload = "{\"nickname\":\"" + nickname + "\",\"model\":\"" + model + "\",\"manufacturer\":\"" + manufacturer + "\"," \
              "\"app_version\":\"" + app_version + "\",\"icon\":\"" + icon + "\"}"
    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
