import requests

API_KEY = "37521c18db5c99411345936fb491a95d"
sehir = "Samsun"

url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&units=metric&lang=tr"

yanit = requests.get(url)
veri = yanit.json()

print("Şehir:", veri["name"])
print("Sıcaklık:", veri["main"]["temp"], "°C")
print("Hava:", veri["weather"][0]["description"])
print("Nem:", veri["main"]["humidity"], "%")