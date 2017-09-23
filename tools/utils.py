#!/usr/bin/env python
import socket
import sqlite3

import config


def knock(host, port):
    """Return BOOLEAN after check PORT on HOST, PORT and HOST must be passed"""
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        skt.connect((host, port))
        skt.shutdown(2)
        return True
    except socket.error:
        return False


class SQLighter:
    def __init__(self, database=config.SQLITE_DB):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self, table):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM table').fetchall()

    def select_single(self, rownum, table):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM table WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self, table):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM table').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
