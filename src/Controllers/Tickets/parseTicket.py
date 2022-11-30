from io import BytesIO
import re

class parseTicket:
    def __init__(self, tickets):
        usr = tickets[84:][:20].rstrip(b'\x00').decode()
        self.username = usr