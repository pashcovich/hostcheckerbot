#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
from bot import BotHandler

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1

bot = BotHandler(config.TG_TOKEN)


def start(chat_id):
    bot.send_message(chat_id, 'Hello here!')


def help(chat_id):
    bot.send_message(chat_id, 'Help!')


def handle_text(chat_id, msg):
    bot.send_message(chat_id, 'Your msg received.')


def ping_host(chat_id, args):
    pass


def who_host(chat_id, args):
    pass


def udp_check(chat_id):
    pass


def tcp_check(chat_id):
    pass


def handle_command(chat_id, command, args=None, user_id=None):
    #print(command)
    if command[1:] == 'start':
        start(chat_id)
    elif command[1:] == 'help':
        help(chat_id)
    elif command[1:] == 'ping':
        ping_host(chat_id, args)
    elif command[1:] == 'dns':
        who_host(chat_id, args)
    elif command[1:] == 'udp_check':
        udp_check(chat_id, args )
    elif command[1:] == 'tcp_check':
        tcp_check(chat_id, args)
    elif command[1:] == 'check_sudo':
        if chat_id in config.ADMIN_LIST:  #users id  in ADMIN_LIST and chat_id  must both be the same type e.x. INT
            bot.send_message(chat_id, "You are the superuser!")
        else:
            bot.send_message(chat_id, "You are not in the superusers list!")

    else:
        bot.send_message(chat_id, "I don't know such command")


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
                    lc_user = lu['message']['from']['id']
                    if 'text' in lu['message']:
                        lm_txt = lu['message']['text']
                        lm_split_txt = lm_txt.split()
                        if lm_txt[0] == "/":
                            if len(lm_split_txt) > 1:
                                handle_command(lc_id, lm_split_txt[0], lm_split_txt[1:])
                            else:
                                handle_command(lc_id, lm_split_txt[0])
                    else:
                        lm_txt = ''
                    if 'entities' in lu['message']:
                        lm_ents = lu['message']['entities']

                    else:
                        lm_ents = []
                        handle_text(lc_id, lm_txt)

                new_offset = lu_id + 1

    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == '__main__':
    main()
