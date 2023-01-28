#брутфорсинг хеша :)
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]
key = hashlib.sha256(b"125").digest()
plain_text = "TOP ULTRA SUPER DUPER SECRET INFORMATION"
plain_text = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(plain_text.encode()))
i = 100
while i < 999:
    i1 = bytes(str(i), 'utf-8')
    key1 = hashlib.sha256(i1).digest()
    iv = cipher_text[:BS]
    cipher = AES.new(key1, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
    print("TRY #", i, " Plain text:", plain_text)
    i += 1
