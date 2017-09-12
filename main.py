#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1a

import config

from bot import BotHandler

bot = BotHandler(config.TG_TOKEN)

def main():

    try:
        while True:
            bot.get_updates(new_offset)

            lu = bot.ge

            print('Received message - User: %(user_id)s , message.text: %(text)s ' % {"user_id": last_chat_id, "text": last_chat_text.lower()})

            new_offset = last_update_id + 1
        except KeyboardInterrupt:
            print('interrupted!')


if __name__ == '__main__':
    main()
