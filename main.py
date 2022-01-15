#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json

base_url = 'https://api.github.com'
user_name = 'elfedyukova'

response = requests.get(f'{base_url}/users/{user_name}/repos')

# сохранение ответа в файл json
with open('data.json', 'w') as f:
    json.dump(response.json(), f)

# выводим на экран список репозиториев пользователя
for i in response.json():
    print(i['name'])


