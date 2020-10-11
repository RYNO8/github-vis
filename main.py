from flask import Flask
from flask_bootstrap import BOOTSTRAP_VERSION, Bootstrap
assert BOOTSTRAP_VERSION == "4.0.0", "please install version 4 (https://pypi.org/project/Flask-Bootstrap4/)"

app = Flask(__name__, template_folder="")
app.secret_key = "5kucTBxUZ2sE3tQsP8TDgS6mp4mYWM34JNNntGfxKgGhzwCj3q8JHQwVVqBsU9sSB5TUM5"
bootstrap = Bootstrap(app)

with app.app_context():
    import Ryan.user_graph
    import Ryan.repo_graph
    
    import Richard.app # login system

    import Blair.user_vis
app.run(debug=True)
