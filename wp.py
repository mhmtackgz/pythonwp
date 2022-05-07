import pywhatkit as whatsapp
from flask import Flask
try:
    whatsapp.sendwhatmsg("+90**********","Bu Mesajı Python Atmıştır :)",23,37)
except:
    print("Hata")
    