API_KEY = ""
REGION = input("Enter Region:\n1.AMERICAS\n2.EUROPE\n3.ASIA\n").upper()
import requests
custom_headers = {"X-Riot-Token" : API_KEY}

#gives name and tag, requests and prints puuid
while True:
    gameName = input("Enter ign: ")
    tagLine = input("Enter tag line: ")
    data = requests.get(f'https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}', headers=(custom_headers))
    if data.status_code==200:
        info = data.json()
        puuid = info["puuid"]
        print(puuid)
        break
    else:
        print("Bad input! or riots fault idk")


