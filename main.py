#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import shelve
import subprocess

import config
import tools.utils as ut
from bot import BotHandler

__author__ = ' Ilya Sosnovskiy - https://github.com/pashcovich'
__version__ = 0.1

bot = BotHandler(config.TG_TOKEN)


def start(chat_id):
    bot.send_message(chat_id, 'Hello here!')


def show_help(chat_id):
    bot.send_message(chat_id, '/ping [host]\n''/port_check [host] [port]\n')


def handle_text(chat_id, msg):
    # исключительно для теста
    shel = shelve.open(config.SHELVE_DB)
    if msg in shel:
        bot.send_message(chat_id, shel[msg])
        shel.close()
    else:
        bot.send_message(chat_id, 'Your msg received.')


def ping_host(chat_id, args=None):
    if args is None:
        bot.send_message(chat_id, 'host must be passed')
    else:
        if len(args) == 1:
            h = args[0]
            if h == '127.0.0.1':
                bot.send_message(chat_id, 'ha ha, very funny, ping yourself')
            else:

                ping_args = "-n 2 -w 1 " if platform.system().lower() == "windows" else "-c 2"
                ping_str = "ping " + " " + ping_args + " " + h
                need_sh = False if platform.system().lower() == "windows" else True

                ping_response = subprocess.call(ping_str, stdout=subprocess.PIPE, shell=need_sh)
                if ping_response == 0:
                    bot.send_message(chat_id, 'Host <b>' + str(h) + '</b> is UP.', parse_mode="HTML")
                else:
                    bot.send_message(chat_id, 'Host <b>' + str(h) + '</b is DOWN.', parse_mode="HTML")


def who_host(chat_id, args):
    pass


def port_check(chat_id, args=None):
    if args is None:
        bot.send_message(chat_id, 'host  and port must be passed')
    else:
        if len(args) == 2:
            h, p = args[0], args[1]
            if ut.knock(h, int(p)):
                bot.send_message(chat_id, 'Port <b>' + str(p) + '</b> on <b>' + str(h) + '</b> is open.',
                                 parse_mode="HTML")
            else:
                bot.send_message(chat_id, 'Port <b>' + str(p) + '</b> on <b>' + str(h) + '</b> is closed or filtered.',
                                 parse_mode="HTML")
        else:
            bot.send_message(chat_id, 'host  and port must be passed')


def handle_command(chat_id, command, args=None):
    # print(command)
    if command[1:] == 'start':
        start(chat_id)
    elif command[1:] == 'help':
        show_help(chat_id)
    elif command[1:] == 'ping':
        ping_host(chat_id, args)
    elif command[1:] == 'dns':
        who_host(chat_id, args)
    elif command[1:] == 'port_check':
        port_check(chat_id, args)
    elif command[1:] == 'check_sudo':
        if chat_id in config.ADMIN_LIST:  # users id in ADMIN_LIST and chat_id  must both be the same type e.x. INT
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
                        pass
                    else:
                        handle_text(lc_id, lm_txt)

                    # пока не знаю зачем, но будем хранить сообщения
                    shel = shelve.open(config.SHELVE_DB)
                    shel[str(lu_id)] = lm_txt
                    shel.close()

                new_offset = lu_id + 1

    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == '__main__':
    main()
