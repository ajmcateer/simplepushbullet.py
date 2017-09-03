import simplepushbullet
import unittest
import os
import json


class UnitTests(unittest.TestCase):

    def test_send_message(self):
        self.assertNotIn('error', simplepushbullet.send_message(title='test', message='send_message', api_key=api_key))

    def test_send_list(self):
        self.assertNotIn('error', simplepushbullet.send_list(title='test', message=['send', 'list', 'test'],
                                                             api_key=api_key))

    def test_get_user(self):
        self.assertNotIn('error', simplepushbullet.get_user(api_key=api_key))

    def test_get_all_devices(self):
        self.assertNotIn('error', simplepushbullet.get_all_devices(api_key=api_key))

    def test_get_pushes(self):
        self.assertNotIn('error', simplepushbullet.get_pushes(api_key=api_key))

    def test_dismiss_push(self):
        res_dict = json.loads(simplepushbullet.send_message(api_key=api_key, title='title', message='dismiss_push'))
        self.assertNotIn('error', simplepushbullet.dismiss_push(api_key=api_key, iden=res_dict["iden"]))

    def test_delete_push(self):
        res_dict = json.loads(simplepushbullet.get_pushes(api_key=api_key, limit=1))
        self.assertNotIn('error', simplepushbullet.delete_push(api_key=api_key, iden=res_dict["pushes"][0]["iden"]))

    def test_create_chat(self):
        self.assertNotIn('error', simplepushbullet.create_chat(api_key=api_key, email='simplepushbullet@gmail.com'))

    def test_list_chat(self):
        self.assertNotIn('error', simplepushbullet.list_chats(api_key=api_key))

    def test_delete_chat(self):
        res_dict = json.loads(simplepushbullet.list_chats(api_key=api_key))
        self.assertNotIn('error', simplepushbullet.delete_chat(api_key=api_key, iden=res_dict['chats'][0]['iden']))

    # def test_

    if __name__ == '__main__':
        unittest.main()


def load_api_key(api_path):
    with open('api_key.txt') as file_contents:
        content = file_contents.read()
    return content

api_path = os.path.join(os.path.dirname(__file__), 'api_key.txt')
api_key = load_api_key(api_path)
