import requests

TOKEN = "8002757650:AAH3HJKUDwYQ_SBTmit7DHEcqW_BF3VHBtg"
CHAT_ID = "842204080"

def mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    veri = {"chat_id": CHAT_ID, "text": mesaj}
    requests.post(url, data=veri)

mesaj_gonder("🤖 Fiyat Takip Botu aktif!")
print("Mesaj gönderildi!")