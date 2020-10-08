from flask import current_app as app
from flask import request, render_template
from github import Github, NamedUser
import pickle
import string
import time

g = Github("test-user1337", "cyrilhas2iq")
MAX_TIME = 5 # bfs() will take <= 5 seconds

def favLanguage(user):
    if isinstance(user, NamedUser.NamedUser):
        return user.login[0].title()
    elif isinstance(user, str):
        return user[0].title()
    else:
        raise
        
def bfs(user):
    """https://en.wikipedia.org/wiki/Breadth-first_search"""
    """NOTE: it would tend to explore friends with more followers"""
    
    # queue
    todo = [user] # list of user objects

    # graph representation
    allUsers = [user] # list of of user objects
    edges = [] # list of tuples representing edges (string, string)
    start = time.time()
    while todo and time.time() - start < MAX_TIME:
        curr = todo.pop(0)
        print("Exploring:", curr)
        
        for child in list(curr.get_followers()):
            if not child in allUsers:
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
            
    [user.bio for user in allUsers] #retrieves bio data, so it can be pickled
    return allUsers, edgeDirection

def sanitise(text):
    return text.replace("'", "\\'").replace("\r\n", "<br>")

@app.route("/user_graph", methods=["GET", "POST"])
def user_graph():
    """\
USAGE
GET /graph?user=RYNO8
POST /graph {"user": "RYNO8"}"""
    user = None
    if request.method == "GET":
        user = request.args.get("user", user)
    elif request.method == "POST":
        user = request.form.get("user", user)
    if not user:
        return sanitise("invalid\n" + user_graph.__doc__)
    print(user)
    
    # cache previous graphs during development / debugging
    try: 
        allUsers, edges = pickle.load(open(f"user_graph_cache\{user}", "rb"))
    except FileNotFoundError:
        allUsers, edges = bfs(g.get_user(user))
        pickle.dump((allUsers, edges), open(f"user_graph_cache\{user}", "wb"))
    
    return render_template(
        "user_graph.html",
        nodeLabels=list(string.ascii_uppercase), #TODO: fix
        nodes=", ".join([f"""{{
            id: {i},
            label: '{user.login}',
            value: {sum(i in edge for edge in edges)**1.3},
            lang: '{favLanguage(user)}',
            shape: 'circularImage',
            image: '{user.avatar_url}',
            {"title: '" + sanitise(user.bio) + "'," if user.bio else ""}
        }}""" for i, user in enumerate(allUsers)]),
        edges=", ".join([f"{{ from: {i[0]}, to: {i[1]}, arrows: '{i[2]}' }}" for i in edges])
    )

