from flask import *

app = Flask(__name__, instance_relative_config=False)
with app.app_context():
    import user_graph
    import repo_graph
app.run(debug=True)
