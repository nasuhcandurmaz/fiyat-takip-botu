import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

TOKEN = "8002757650:AAH3HJKUDwYQ_SBTmit7DHEcqW_BF3VHBtg"
CHAT_ID = "842204080"

def mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    veri = {"chat_id": CHAT_ID, "text": mesaj}
    requests.post(url, data=veri)

conn = sqlite3.connect("fiyatlar.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS urunler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT,
        fiyat REAL,
        tarih TEXT
    )
""")

url = "https://books.toscrape.com"
sayfa = requests.get(url)
soup = BeautifulSoup(sayfa.content, "html.parser")
kitaplar = soup.find_all("article", class_="product_pod")

for kitap in kitaplar[:5]:
    isim = kitap.h3.a["title"]
    fiyat_text = kitap.find("p", class_="price_color").text
    fiyat = float(fiyat_text.replace("£", "").replace("Â", "").strip())
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute("SELECT fiyat FROM urunler WHERE isim = ? ORDER BY id DESC LIMIT 1", (isim,))
    onceki = cursor.fetchone()

    if onceki:
        if fiyat < float(onceki[0]):
            mesaj = f"🔻 FİYAT DÜŞTÜ!\n{isim}\nEski: £{onceki[0]}\nYeni: £{fiyat}"
            print(mesaj)
            mesaj_gonder(mesaj)
        elif fiyat > float(onceki[0]):
            print(f"🔺 Fiyat arttı: {isim}")
        else:
            print(f"✅ Değişmedi: {isim}")
    else:
        print(f"🆕 İlk kayıt: {isim} - £{fiyat}")

    cursor.execute("INSERT INTO urunler (isim, fiyat, tarih) VALUES (?, ?, ?)",
                   (isim, fiyat, tarih))

conn.commit()
conn.close()