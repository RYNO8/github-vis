from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=False, template_folder="")
app.secret_key="5kucTBxUZ2sE3tQsP8TDgS6mp4mYWM34JNNntGfxKgGhzwCj3q8JHQwVVqBsU9sSB5TUM5"
bootstrap = Bootstrap(app)

with app.app_context():
    import Ryan.user_graph
    import Ryan.repo_graph
    
    import Richard.app # login system

    import Blair.user_vis
app.run(debug=True)
