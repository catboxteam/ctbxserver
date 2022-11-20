from io import BytesIO
import re

class parseTicket:
    def __init__(self, tickets):
        buffer = BytesIO()
        ticket = bytes(tickets)
        buffer.write(ticket)

        buffer.seek(84)
        b = buffer.read(20).decode()
        self.username = re.sub('[^!-~]+',' ',b).strip()