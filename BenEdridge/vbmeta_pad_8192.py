import hashlib
import sys

f = open("vbmeta.gmi", "rb")

b = f.read()

sha = hashlib.sha256(b).digest()

f.close()
f = open("vbmeta.gmi", "wb")
f.write(b)

f.seek(1048576 - 512)

f.write(b'\x44\x48\x54\x42\x01\x00\x00\x00')
f.write(sha)
f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00')
f.seek(1048576 - 1)
f.write(b'\x00')
f.close()
