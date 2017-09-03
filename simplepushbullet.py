"""A simple Pushbullet interface"""
import requests
import json


def get_user(api_key):
    url = "https://api.pushbullet.com/v2/users/me"

    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers)

    return response.text


def send_message(title, message, api_key):
    """Sends text note to pushbullet notification"""

    url = "https://api.pushbullet.com/v2/pushes"
    payload = json.dumps({"body": message, "title": title, "type": "note"})

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
    payload = json.dumps({'body': message_str, 'title': title, "type": "note"})
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

    payload = json.dumps({'limit': limit, 'active': active, 'modified_after': modified_after})

    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }
    response = requests.request("GET", url, params=payload, headers=headers)

    return response.text


def dismiss_push(api_key, iden):
    url = "https://api.pushbullet.com/v2/pushes/" + iden

    payload = json.dumps({'dismissed': True})

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

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


def create_device(api_key, nickname="", model="", manufacturer="", app_version="", icon="desktop"):

    url = "https://api.pushbullet.com/v2/devices"

    # Can't get has_sms = true working hard coding to false till I figure it out leaving code to handle it though
    has_sms = "false"

    if has_sms == "true":
        payload = json.dumps({'nickname': nickname, 'model': model, 'manufacturer': manufacturer, 'app_version': app_version,
                   'icon': icon, 'has_sms': has_sms})
    else:
        payload = json.dumps({'nickname': nickname, 'model': model, 'manufacturer': manufacturer, 'app_version': app_version,
                   'icon': icon})
    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


def list_chats(api_key):
    url = "https://api.pushbullet.com/v2/chats"

    headers = {
        'access-token': api_key,
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)

    return response.text


def create_chat(api_key, email):
    url = "https://api.pushbullet.com/v2/chats"

    payload = json.dumps({'email': email})
    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


def update_chat(api_key, mute, iden):
    url = "https://api.pushbullet.com/v2/chats" + iden

    payload = json.dumps({'mute': mute})
    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


def delete_chat(api_key, iden):
    url = "https://api.pushbullet.com/v2/chats/" + iden

    headers = {
        'access-token': api_key,
        'content-type': "application/json"
    }

    response = requests.request("DELETE", url, headers=headers)

    return response.text

# print(send_message('', '', 'o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930'))
# print(create_chat(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930', email='simplepushbullet@gmail.com'))
# print(list_chats(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930'))
# print(delete_chat(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930', iden='ujvjcr9H6I0sjAdVpR3rsi'))
# res_dict = json.loads(list_chats(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930'))
# print(delete_chat(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930', iden='ujvjcr9H6I0sjArp1yiWn6'))
# print(get_pushes(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930', limit=1))
# print(dismiss_push(api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930', iden='ujvjcr9H6I0sjAbY5QZdy8'))
# print(send_list(title='test', message=['1', '2', '3'], api_key='o.x8wWqf9X4j7jywUMqBss5NGZlNFb1930'))