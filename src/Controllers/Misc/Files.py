import zlib,struct,io,imghdr
from PIL import Image,ImageFile
from enum import Enum
ImageFile.LOAD_TRUNCATED_IMAGES = True

class fileType(Enum):
    Texture = 1
    Level = 2
    Plan = 3
    Jpeg = 4
    Png = 5
    Voip = 6
    Unknown = -1

class LBPFile:
    def __init__(self,file) -> None:
        self.file = file

    @property
    def fileType(self):
        global f
        try:
            # f = open(self.file,"rb").read()[:3].decode()
            
            f = self.file[:4].decode()

            match f:
                case "TEX ":
                    return fileType.Texture
                case "PLNb":
                    return fileType.Plan
                case "LVLb":
                    return fileType.Level
                case "VOPb":
                    return fileType.Voip
                case _:
                    return f
            
            # return f
        except UnicodeDecodeError:
            d = io.BytesIO(self.file)
            # print(d)
            if imghdr.what(d) == "jpeg":
                return fileType.Jpeg
            else:
                return None

    def safeFile(self):
        match self.fileType:
            case fileType.Texture:
                return True
            case fileType.Plan:
                return True
            case fileType.Voip:
                return True
            case _:
                d = io.BytesIO(self.file)
                # print(d)
                if imghdr.what(d) == "jpeg":
                    return True
                else:
                    return False

    def decompressFile(self,name):
        #https://github.com/LBPUnion/ProjectLighthouse/blob/a2828337261b90fb1b089eb3ff7ce56430a359b7/ProjectLighthouse/Files/FileHelper.cs#L364
        try:
            reader = io.BytesIO(self.file)
            for _ in range(3):
                reader.read(1)

            if chr(reader.read(1)[0]) != " ":
                return False

            reader.read(2)

            chunks = reader.read(2)
            chunks = struct.unpack(">h", chunks)[0]

            compressed = [0] * chunks
            decompressed = [0] * chunks

            for i in range(chunks):
                compressed[i] = struct.unpack(">H", reader.read(2))[0]
                decompressed[i] = struct.unpack(">H", reader.read(2))[0]

            ms = bytearray()
            for i in range(chunks):
                deflated_data = reader.read(compressed[i])
                if compressed[i] == decompressed[i]:
                    ms += deflated_data
                    continue

                inflater = zlib.decompressobj()
                inflated_data = inflater.decompress(deflated_data)

                ms += inflated_data


                f = io.BytesIO(ms)
                Image.open(f).save(f"png/{name}.png", "PNG")

                # open(f"png/{name}.dds","wb").write(ms)
        except Exception as e:
            print(f"{name} not converted because {e}")