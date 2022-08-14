import base64
from fileinput import filename


def encodeb6(filez):
    name = ".\\plugin\\"+filez
    with open(name , "rb") as f:
        bytes = f.read()
        encode_string = base64.b64encode(bytes)
    
    with open('.\\work_dir\\file.txt' , "wb") as result:
        result.write(encode_string)


encodeb6(filez= "upload.py")