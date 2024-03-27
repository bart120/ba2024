import requests

url_root = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines"

reponse = requests.get(url_root)

contenu = reponse.json()

print(contenu)
