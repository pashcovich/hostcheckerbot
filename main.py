#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
from bot import BotHandler

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1

bot = BotHandler(config.TG_TOKEN)


def start(chat_id):
    bot.send_message(chat_id, 'Hello here!')


def handle_text(text):
    pass


def handle_command(command):
    if command[1:] == 'start':
        start()
    else:
        pass



def main():
    new_offset = None

    try:
        while True:
            bot.get_updates(new_offset)
            lu = bot.get_last_update()

            if lu is not None:
                lu_id = lu['update_id']

                if "message" in lu:
                    lc_id = lu['message']['chat']['id']
                    lc_username = lu['message']['from']
                    if 'text' in lu['message']:
                        lc_txt = lu['message']['text']
                    else:
                        lc_txt = ''
                    if 'entities' in lu['message']:
                        lm_ents = lu['message']['entities']
                    else:
                        lm_ents = []

                new_offset = lu_id + 1

    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == '__main__':
    main()
