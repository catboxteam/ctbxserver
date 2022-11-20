from datetime import datetime
import time
import os.path
class Misc:
    
    def checkFile(hash):
        return os.path.exists(f"r/{hash}")

    def timestamp():
        millisecond = datetime.now()
        timez = time.mktime(millisecond.timetuple()) * 1000
        return timez
