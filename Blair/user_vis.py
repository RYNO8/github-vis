#### TODO ####
# todo contributor list on right?

#links:
#parameter passing in urls: https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
#table for ronald's pg: https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
from flask import current_app as app

from flask import Flask, render_template, request, jsonify
import requests
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from .form1 import Form
import json
import webbrowser
import github

# Pie chart imports
from math import pi
from bokeh.transform import cumsum
from bokeh.plotting import figure, ColumnDataSource
from bokeh.embed import components


# g = github.Github("test-user1337", "cyrilhas2iq")
# print(g.get_user())


auth = ("my_client_id", "")
def_header = {"Accept": "application/vnd.github.v3+json"}



def get_user(url, user, headers=def_header):
    result = requests.get(f"https://api.github.com/users/{user}{url}", headers=headers).json()
    return result


def get_repo(url, owner, repo, headers=def_header):
    result = requests.get(f"https://api.github.com/repos/{owner}/{repo}/{url}", headers=headers).json()
    return result


@app.route("/blairstupid", methods=["GET", "POST"])
def index():
    form = Form()
    if request.method == "POST":
        details = request.form
        return "hello world! ur using the wrong path"
    return render_template("Blair/templates/index.html", form=form)


def fav_lang(repos):
    FavLang = "None"
    langs = {}
    for repo in repos:
        langs[repo["language"]] = langs.get(repo["language"], 0) + 1
    maxFreq = 0
    for lang, freq in langs.items():
        if freq > maxFreq:
            FavLang = lang
            maxFreq = freq
    return FavLang


def badUser(user):
    return render_template("badSearch.html", type="user", name=user)


@app.route("/users", methods=["GET"])
def ryanSync():
    user = request.args.get("user", "RYNO8")
    print(user)
    User_info = get_user(url="", user=user)
    if User_info.get("message", False):
        print(User_info["message"])
        return badUser(user)
    User_repos = get_user("/repos", user)
    User_repos.sort(key=lambda x: x["stargazers_count"], reverse=True) #most stargazers come first
    favLang = fav_lang(User_repos)
    print(User_info)
    print(User_repos)
    return render_template("Blair/templates/submit.html", repos=User_repos, user_info=User_info, favLang=favLang)


def pi_chart(result): #ronalds part
    sum = 0
    languages = []
    percentages = []
    angles = []
    palette = ["#00009C", "#00BFFF", "#00AF33", "#551011",
               "#691F01", "#88ACE0", "#B62084", "#C0FF3E", "#CD3333"]
    for key, value in result.items():
        sum += value
    for key, value in result.items():
        percentage = round(value/sum*100,2)
        angle = percentage*pi/50

        languages.append(key)
        percentages.append(percentage)
        angles.append(angle)
    # print(languages)
    # print(percentages)
    # print(angles)

    everything = {
        "languages": languages,
        "percent": percentages,
        "angle": angles,
        "colours": palette[:len(languages)]
    }
    source = ColumnDataSource(data=everything)
    TOOLTIPS = "@languages: @percent%"

    p = figure(plot_height=350, title="Languages Used", toolbar_location=None,
               tools="hover", tooltips=TOOLTIPS, x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='colours', source=source)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    p.outline_line_color = None

    return components(p)


def badRepo(repo):
    return render_template("badSearch.html", type="repo", name=repo)


@app.route("/ronaldsubmit", methods=["GET"])
def ronaldSync():
    Owner = request.args.get("owner")
    Repo = request.args.get("repo")
    languages = get_repo("languages", Owner, Repo)
    if languages.get("message", False):
        print(languages["message"])
        return badRepo(Repo)
    print(languages)
    contributors = get_repo("contributors", Owner, Repo)
    conts = [contributor["contributions"] for contributor in contributors]
    total = sum(conts)
    pi_script, pi_div = pi_chart(languages)
    return render_template("Blair/templates/ronaldsubmit.html", pi_script=pi_script, pi_div=pi_div, contributors=contributors, total=total, owner=Owner, repo=Repo)

if __name__ == "__main__":
    raise Exception("Don't run this file on its own. run main.py from the root directory")
