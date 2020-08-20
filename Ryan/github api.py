
'''from github import Github

# First create a Github instance:

# using username and password
g = Github("ryno8",                                                                                                                                         "1qSX2wDC")

# or using an access token
#g = Github("access_token")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)'''



import requests
from pprint import pprint
import json

def recentUsers():
    """https://docs.github.com/en/rest/reference/users#list-users"""
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get('https://api.github.com/users', headers=headers)
    return response.json()


def getUser(user):
    """https://docs.github.com/en/rest/reference/users#get-a-user"""
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(f'https://api.github.com/users/{user}', headers=headers)
    return response.json()

def getUserInfo(user):
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(f'https://api.github.com/users/{user}/hovercard', headers=headers)
    return response.json()

def getFollowing(user): #outgoing edges
    response = requests.get(f"https://api.github.com/users/{user}/following")
    return [i["login"] for i in response.json()]

def getFollowers(user): #ingoing edges
    response = requests.get(f"https://api.github.com/users/{user}/followers")
    return [i["login"] for i in response.json()]


#graph = {}
#todo = ["RYNO8"]
#seen = set()
graph = eval(open("graph.txt", "r").readline())
todo = open("todo.txt", "r").readline().split(" ")
seen = set(open("seen.txt", "r").readline().split(" "))

def addPath(a, b):
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)

def save():
    open("graph.txt", "w").write(str(graph).replace("{}", "set()"))
    open("todo.txt", "w").write(" ".join(todo))
    open("seen.txt", "w").write(" ".join(list(seen)))

for rep in range(500): #get 500 other users
    curr = todo.pop(0)
    print(curr)
    
    for child in getFollowing(curr):
        addPath(curr, child)
        if child not in seen:
            todo.append(child)
            seen.add(child)
            
    for child in getFollowers(curr):
        addPath(child, curr)
        if curr not in graph:
            todo.append(child)
            seen.add(child)
        

#print(getFollowing("ryno8"))
#print(getFollowers("ryno8"))
