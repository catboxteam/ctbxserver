from Controllers.Misc.Files import LBPFile,fileType
import os
# path = 'r/'


count = 0
for filename in os.listdir("r"):
    file_path = os.path.join('r/', filename)
    f = LBPFile(open(file_path,"rb").read())
    # print(f"{f.fileType} | {f.safeFile()}")
    if f.fileType == fileType.Texture:
        count +=1
        f.decompressFile(filename)

print(f"Successfully converted {count} images")