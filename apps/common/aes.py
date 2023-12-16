import base64
import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rest_framework.renderers import BaseRenderer

from config.env import env

AES_SECRET_KEY = bytes(env("AES_SECRET_KEY"), "utf-8")
AES_IV = bytes(env("AES_IV"), "utf-8")


class CustomAesRenderer(BaseRenderer):
    media_type = "application/octet-stream"
    format = "aes"

    def render(self, data, media_type=None, renderer_context=None):
        plaintext = json.dumps(data)
        padded_plaintext = pad(plaintext.encode(), 16)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        ciphertext = cipher.encrypt(padded_plaintext)
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        response = {"ciphertext": ciphertext_b64}
        return json.dumps(response)
