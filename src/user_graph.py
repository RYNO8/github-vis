import os
from flask import current_app as app
from flask import request, render_template, session
from github import Github, NamedUser
import pickle
import time
import requests

def getx(self): return self._x
def setx(self, value): self._x = value
def delx(self): del self._x
NamedUser.NamedUser._x = None    
NamedUser.NamedUser.language = property(getx, setx, delx, "Users favourite language")
HEADERS = {"Accept": "application/vnd.github.v3+json"} #, "Authorization": "token c1b45bdfa9efd656883a4b936de140261e94f8c1"}

MAX_TIME = 5 # bfs() will take <= 5 seconds

def favLanguage(user):
    #return "A" #stub
    if not isinstance(user, str):
        user = user.login
    print("getting language for", user)
    langs = {}
    repos = requests.get(f"https://api.github.com/users/{user}/repos", headers=HEADERS)
    for repo in repos.json():
        langs[repo["language"]] = langs.get(repo["language"], 0) + 1
    if None in langs: del langs[None]
    
    # find most frequent language
    for language, freq in langs.items():
        if freq == max(langs.values()):
            return language
    return "None" # as a string for consistancy

def bfs(user):
    """https://en.wikipedia.org/wiki/Breadth-first_search"""
    """NOTE: it would tend to explore friends with more followers"""
    user.language = favLanguage(user)
    
    # queue
    todo = [user] # list of user objects

    # graph representation
    allUsers = [user] # list of of user objects
    edges = [] # list of tuples representing edges (string, string)
    start = time.time()
    while todo and time.time() - start < MAX_TIME:
        curr = todo.pop(0)
        print("Exploring:", curr, time.time() - start)
        
        for child in list(curr.get_followers()):
            if not child in allUsers:
                child.bio #retrieves bio data, so it can be pickled
                child.language = favLanguage(child)
                assert child not in allUsers
                todo.append(child)
                allUsers.append(child)
            edges.append((allUsers.index(curr), allUsers.index(child)))
    
    # find bidrectional edges. if a->b and b->a, a<->b
    edgeDirection = []
    while edges:
        curr = edges.pop()
        if (curr[1], curr[0]) in edges: # edge is bidirectional
            edges.remove((curr[1], curr[0]))
            edgeDirection.append((*curr, "to, from"))
        else: # edge is not bidirectional
            edgeDirection.append((*curr, "to"))
    
    return allUsers, edgeDirection

def sanitise(text):
    return text.replace("'", "\\'").replace("\r\n", "<br>").replace("\n", "<br>")

@app.route("/user_graph", methods=["GET", "POST"])
def user_graph():
    """\
USAGE
GET /user_graph?user=RYNO8
POST /user_graph {"user": "RYNO8"}"""
    user = None
    if request.method == "GET":
        user = request.args.get("user", user)
    elif request.method == "POST":
        user = request.form.get("user", user)
    if not user:
        return sanitise("invalid\n" + user_graph.__doc__)

    if "access_token" in session and session["access_token"]:
        g = Github(session["access_token"])
    else:
        g = Github("test-user1337", "cyrilhas2iq")
        
    # cache previous graphs to reduce number of api calls
    try:
        allUsers, edges = pickle.load(open(f"user_graph_cache\\{user}", "rb"))
    except FileNotFoundError:
        allUsers, edges = bfs(g.get_user(user))
        pickle.dump((allUsers, edges), open(f"user_graph_cache\\{user}", "wb"))
        
    all_languages = set()
    for user in allUsers:
        all_languages.add(user.language)
    return render_template(
        "user_graph.html",
        nodeLabels=sorted(list(all_languages)),
        nodes=", ".join([f"""{{
            id: {i},
            label: '{user.login}',
            value: {sum(i in edge for edge in edges)**1.3},
            lang: '{user.language}',
            shape: 'circularImage',
            image: '{user.avatar_url}',
            {"title: '" + sanitise(user.bio) + "'," if user.bio else ""}
        }}""" for i, user in enumerate(allUsers)]),
        edges=", ".join([f"{{ from: {i[0]}, to: {i[1]}, arrows: '{i[2]}' }}" for i in edges])
    )

if __name__ == "__main__":
    raise Exception("Don't run this file on its own. run main.py from the root directory")
