import requests

url_root = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines"

code_commune = 95500
url_api = f'{url_root}?qs=code_insee_commune_actualise:"{code_commune}"'
#url_api = url_root + '?qs=code_insee_commune_actualise:"' + str(code_commune)+'"'
reponse = requests.get(url_api)

contenu = reponse.json()

print(contenu)



# python -m pip install requests
#https://pythononlinecompiler.com/