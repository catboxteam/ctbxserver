from datetime import datetime
import time
class Misc():
    def timestamp():
        millisecond = datetime.now()
        timez = time.mktime(millisecond.timetuple()) * 1000
        return timez
