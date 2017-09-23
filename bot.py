#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import requests

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1

loger = logging.getLogger()
loger.setLevel(logging.INFO)
log_format = logging.Formatter("%(asctime)s  [%(levelname)-5.5s]  %(message)s")

logPath = './logs/'
logFile = 'bot'

fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, logFile))
fileHandler.setFormatter(log_format)
loger.addHandler(fileHandler)


class BotHandler:
    def __init__(self, token=None):
        if token is None:
            raise ValueError('`token` must be passed')
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

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            loger.info(get_result)
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update
