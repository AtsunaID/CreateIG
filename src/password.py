import base64
import struct
import datetime
import binascii
from urllib.parse import quote_plus
from Cryptodome import Random
from Cryptodome.Cipher import AES
from nacl.public import PublicKey, SealedBox

key_id ,pub_key = log()
password = pw()
def encrypt_password(key_id, pub_key, password, version=10):
  key = Random.get_random_bytes(32)
  iv = bytes([0] * 12)
  time = int(datetime.datetime.now().timestamp())
  aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
  aes.update(str(time).encode('utf-8'))
  encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))
  pub_key_bytes = binascii.unhexlify(pub_key)
  seal_box = SealedBox(PublicKey(pub_key_bytes))
  encrypted_key = seal_box.encrypt(key)
  encrypted = bytes([1,
    key_id,
    *list(struct.pack('<h', len(encrypted_key))),
    *list(encrypted_key),
    *list(cipher_tag),
    *list(encry
  )])
  encrypted = base64.b64encode(encrypted).decode('utf-8')
  return quote_plus(f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}')

