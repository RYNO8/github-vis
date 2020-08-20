from flask import *

app = Flask(__name__)
@app.route("/")
def main():
    graph = eval(open("graph_smol.txt", "r").readline())
    allUsers = set()
    edges = set()
    for sNode, eNodes in graph.items():
        allUsers.add(sNode)
        for eNode in eNodes:
            edges.add((sNode, eNode))
            allUsers.add(eNode)
    nameToNode = {v: k for k, v in enumerate(allUsers)}
    #nodeToName = {k: v for k, v in enumerate(graph.keys())}
    
    return render_template(
        "network vis.html",
        nodes=", ".join([f"{{id: {v}, label: '{k}'}}" for k, v in nameToNode.items()]),
        edges=", ".join([f"{{from: {nameToNode[k]}, to: {nameToNode[v]}}}" for k, v in edges])
    )

app.run(debug=True)


# GET /submit user=...
