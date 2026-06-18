import requests

url = "https://www.kratc.lt/produktai/mainu-stotele-imk/klaipeda/"

r = requests.get(url, timeout=30)

print(r.status_code)

if r.status_code == 200:
    print("KRATC puslapis pasiekiamas")
else:
    print("Klaida")
