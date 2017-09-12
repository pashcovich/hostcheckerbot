#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1

import config

from bot import BotHandler

bot = BotHandler(config.TG_TOKEN)


def handle_text(text):
    pass


def handle_command(command):
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
                    if 'text' in lu['message']:
                        lc_txt = lu['message']['text']
                    else:
                        lc_txt = ''
                    if 'entities' in lu['message']:
                        lm_type = lu['message']['entities'][0]['type']
                    else:
                        lm_type = 'usual'

                    print('New msg - User: %(uid)s, msg.type: %(type)s, msg.text: %(txt)s ' % {"uid": lc_id, "type": lm_type, "txt": lc_txt.lower()})

                new_offset = lu_id + 1

    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == '__main__':
    main()
