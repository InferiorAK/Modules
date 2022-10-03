# Published Date: 4th Oct 2022 (GMT+6)
#. Copyright (C) 2022   Mi Taseen

__doc__ = """
    Mihash v.1
****************
The Module is Used for Hash Encoding and Decoding


copyright: (c) 2022 by Mi Taseen
license: Apache License 2.0, see LICENSE for more details.

"""

from hashlib import *
import os
from color import *

"""
Hash_Types:
------------
    md5
    sha256
    sha224
    sha256
    sha384
    sha512
    blake2b
    blake2s
    sha3_224
    sha3_256
    sha3_384
    sha3_512
    shake_128
    shake_256

Encoding_Types:
----------------
    byte
    hex

"""

suc = "[Found!]"
fck = "[Failed!]"

def encrypt(text, format, encoding):
    """Encode a String to Hash
    
    Usage::
    
      >>> import Mihash
      >>> Mihash.encrypt('Hello World', md5, 'byte')
      >>> b10a8db164e0754105b7a99be72e3fe5

    """
    if encoding == "byte":
        hash_byte = format(text.encode()).digest()
        print(g+str(hash_byte))
    elif encoding == "hex":
        hash_hex = format(text.encode()).hexdigest()
        print(g+hash_hex)
    else:
        print("Define Encoding: 'byte' or 'hex'")

def encrypt_file(file, format, encoding, out_file):
    """Encode a file to Hashed file
    
    Usage::
    
      >>> import Mihash
      >>> Mihash.encrypt_file('app.jpg', md5, 'byte', 'app.out')

    """
    file = open(file,"rb")
    if os.path.exists(out_file):
        outfile = out_file+"{}"
        cnt = 1
        while os.path.exists(outfile.format(cnt)):
            cnt += 1
        outfile = outfile.format(cnt)
        if encoding == "byte":
            for line in file:
                hash_byte = format(line).digest()
                with open(outfile,"ab") as out:
                    out.write(hash_byte)
                    out.close()
        elif encoding == "hex":
            for line in file:
                hash_hex = format(line).hexdigest()
                with open(outfile,"a") as out:
                    out.write(hash_hex)
                    out.close()
        else:
            print("Define Encoding: 'byte' or 'hex'")
    else:
        if encoding == "byte":
            for line in file:
                hash_byte = format(line).digest()
                with open(out_file,"ab") as out:
                    out.write(hash_byte)
                    out.close()
        elif encoding == "hex":
            for line in file:
                hash_hex = format(line).hexdigest()
                with open(out_file,"a") as out:
                    out.write(hash_hex)
                    out.close()
        else:
            print("Define Encoding: 'byte' or 'hex'")


def decrypt(hash, format, wordlist):
    """Decode a Hash to String
    
    Usage::
    
      >>> import Mihash
      >>> Mihash.decrypt('b10a8db164e0754105b7a99be72e3fe5', md5, 'wordlist.txt')
      >>> Hello World

    """
    wd = open(wordlist)
    cnt = 0
    for line in wd:
        word = line.split("\n")[0]
        cnt += 1
        ser = str(cnt)+". "
        enc = format(word.encode()).hexdigest()
        if enc == hash:
            print(f"{g}{ser}{word} {suc}")
            break
        else:
            print(f"{r}{ser}{word} {fck}")

if __name__ == "__main__":
    print(__doc__)
    print(y+encrypt.__doc__)
    print(y+encrypt_file.__doc__)
    print(y+decrypt.__doc__)
