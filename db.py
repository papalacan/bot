#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pony.orm import *

lacanDB = Database()
class Chat(lacanDB.Entity):
    primary_id = PrimaryKey(int, auto=True)
    chat_id = Required(int, size=64, unique=True)
    user_id = Required(int)
    open_date = Required(datetime)
    last_message_date = Optional(datetime)
    username = Optional(str)
    first_name = Optional(str)
    last_name = Optional(str)
    silent_mode = Required(bool)
    deleted = Required(bool)
