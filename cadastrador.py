#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Criador: Alvaro


import sqlite3
import re


def regexp(y, x, search=re.search):
    """REGEX para SQLite"""
    return True if search(y, x) else False


conn = sqlite3.connect('Database.db')
conn.create_function("REGEXP", 2, regexp)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pessoas(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Cel VARCHAR(15) NOT NULL,
    Nasc VARCHAR(12) NOT NULL,
    Grad VARCHAR(15) NOT NULL);
    ''')
