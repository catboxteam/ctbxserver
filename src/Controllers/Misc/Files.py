import imghdr
import io


class LBPFile:
    def __init__(self,file) -> None:
        self.file = file

    @property
    def fileType(self):
        global f
        try:
            # f = open(self.file,"rb").read()[:3].decode()
            f = self.file[:4].decode()
            
            return f
        except UnicodeDecodeError:
            d = io.BytesIO(self.file)
            # print(d)
            if imghdr.what(d) == "jpeg":
                return  "JPG "
            else:
                return None

    def safeFile(self):
        match self.fileType:
            case "TEX ":
                return True
            case "PLNb":
                return True
            case _:
                d = io.BytesIO(self.file)
                # print(d)
                if imghdr.what(d) == "jpeg":
                    return True
                else:
                    return False

