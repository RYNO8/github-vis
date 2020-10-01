from flask import *
from github import Github, NamedUser
import pickle
import string

app = Flask(__name__)
g = Github("test-user1337", "cyrilhas2iq")
SEARCH_NODES = 20

def favLanguage(user):
    if isinstance(user, NamedUser.NamedUser):
        return user.login[0].title()
    elif isinstance(user, str):
        return user[0].title()
    else:
        raise
        
def bfs(user):
    """treats all edges as bidirectional edges based on followers (not followings)"""
    #time taken exponential to DEPTH and len(followers)
    
    todo = [user] # list of user objects
    allUsers = [user] # list of of user objects
    edges = [] # list of tuples representing edges (string, string)
    for depth in range(SEARCH_NODES):
        curr = todo.pop(0)
        print(curr)
        
        for child in list(curr.get_followers()):
            if not child in allUsers:
                todo.append(child)
                allUsers.append(child)
            edges.append((allUsers.index(curr), allUsers.index(child)))
            
    edgeDirection = []
    while edges:
        curr = edges.pop()
        if (curr[1], curr[0]) in edges: # edge is bidirectional
            edges.remove((curr[1], curr[0]))
            edgeDirection.append((*curr, "to, from"))
        else: # edge is not bidirectional
            edgeDirection.append((*curr, "to"))
    
    return allUsers, edgeDirection

@app.route("/graph", methods=["GET", "POST"])
def main():
    """\
get request: view graph for default user ("RYNO8")
post request {"user": x}: view graph for user x"""
    user = "RYNO8"
    if request.method == "GET":
        user = request.args.get("user", user)
    elif request.method == "POST":
        user = request.form.get("user", user)
    print(user)
    
    try:
        allUsers, edges = pickle.load(open(f"cache\{user}", "rb"))
    except FileNotFoundError:
        allUsers, edges = bfs(g.get_user(user))
        
    with open(f"cache\{user}", "wb") as f:
        pickle.dump((allUsers, edges), f)
    
    return render_template(
        "network vis.html",
        nodeLabels=list(string.ascii_uppercase), #TODO: fix
        nodes=", ".join([f"""{{
            id: {i},
            label: '{user.login}',
            value: {sum(i in edge for edge in edges)**1.3},
            lang: '{favLanguage(user)}',
            shape: 'circularImage',
            image: '{user.avatar_url}',
            title: 'TODO: tooltip text',
        }}""" for i, user in enumerate(allUsers)]),
        edges=", ".join([f"{{ from: {i[0]}, to: {i[1]}, arrows: '{i[2]}' }}" for i in edges])
    )

app.run(debug=True)

