from github import Github
import requests

def collect_data(directory):
    baseURL = 'https://api.github.com/'
    routeURL = baseURL + directory
    response = requests.get(routeURL)
    if response.status_code != 200:
        print("Couldn't get data")
    else:
        data = json.loads(response.text)
        return data

g = Github("RichardBao1","435876897Richardbao")
for repo in g.get_user().get_repos():
    print(repo.name)

username = 'RichardBao1'
token = 'token'
login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username, token))
print(login)

import requests
r = requests.get('https://github.com/timeline.json')
r.json()