#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1a

import requests

class BotHandler:
    def __init__(self, token=None):
        if token is None:

        else:
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text, parse_mode=None):

        if parse_mode is None:
            params = {'chat_id': chat_id, 'text': text}
        else:
            params = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}

        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp