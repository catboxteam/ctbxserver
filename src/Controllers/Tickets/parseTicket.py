from io import BytesIO
import re
import struct


class parseTicket:
    def __init__(self, tickets):
        usr = tickets[84:][:20].rstrip(b'\x00').decode()
        self.username = usr
        self.titleId = tickets[136:][:19].decode()