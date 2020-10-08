##### TODO ####
# implement user visualisation from url: /users?user=[username here]
# find a better url name on line 54 (you cant have it at "/")

from flask import current_app as app

from flask import Flask, render_template, request, jsonify
import requests
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from .form1 import Form
import json
import webbrowser


auth = ("my_client_id", "")
def_owner = "octocat"
def_repo = "hello-world"
others = [("indy256", "codejam-templates"), ("NZIO", "nztrain")]
def_header = {"Accept": "application/vnd.github.v3+json"}


def get_user(url, user=def_owner, headers=def_header):
    result = requests.get(f"https://api.github.com/users/{user}{url}", headers=headers).json()
    return result


def get_repo(url, owner=def_owner, repo=def_repo, headers=def_header):
    result = requests.get(f"https://api.github.com/repos/{owner}/{repo}/{url}", headers=headers).json()
    return result


# res = get_user("/repos", "RYNO8")
# print(res)
res = [{'id': 174899437, 'node_id': 'MDEwOlJlcG9zaXRvcnkxNzQ4OTk0Mzc=', 'name': 'Inquit', 'full_name': 'RYNO8/Inquit', 'private': False, 'owner': {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/RYNO8/Inquit', 'description': 'An unblocked messaging app', 'fork': False, 'url': 'https://api.github.com/repos/RYNO8/Inquit', 'forks_url': 'https://api.github.com/repos/RYNO8/Inquit/forks', 'keys_url': 'https://api.github.com/repos/RYNO8/Inquit/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/RYNO8/Inquit/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/RYNO8/Inquit/teams', 'hooks_url': 'https://api.github.com/repos/RYNO8/Inquit/hooks', 'issue_events_url': 'https://api.github.com/repos/RYNO8/Inquit/issues/events{/number}', 'events_url': 'https://api.github.com/repos/RYNO8/Inquit/events', 'assignees_url': 'https://api.github.com/repos/RYNO8/Inquit/assignees{/user}', 'branches_url': 'https://api.github.com/repos/RYNO8/Inquit/branches{/branch}', 'tags_url': 'https://api.github.com/repos/RYNO8/Inquit/tags', 'blobs_url': 'https://api.github.com/repos/RYNO8/Inquit/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/RYNO8/Inquit/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/RYNO8/Inquit/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/RYNO8/Inquit/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/RYNO8/Inquit/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/RYNO8/Inquit/languages', 'stargazers_url': 'https://api.github.com/repos/RYNO8/Inquit/stargazers', 'contributors_url': 'https://api.github.com/repos/RYNO8/Inquit/contributors', 'subscribers_url': 'https://api.github.com/repos/RYNO8/Inquit/subscribers', 'subscription_url': 'https://api.github.com/repos/RYNO8/Inquit/subscription', 'commits_url': 'https://api.github.com/repos/RYNO8/Inquit/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/RYNO8/Inquit/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/RYNO8/Inquit/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/RYNO8/Inquit/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/RYNO8/Inquit/contents/{+path}', 'compare_url': 'https://api.github.com/repos/RYNO8/Inquit/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/RYNO8/Inquit/merges', 'archive_url': 'https://api.github.com/repos/RYNO8/Inquit/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/RYNO8/Inquit/downloads', 'issues_url': 'https://api.github.com/repos/RYNO8/Inquit/issues{/number}', 'pulls_url': 'https://api.github.com/repos/RYNO8/Inquit/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/RYNO8/Inquit/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/RYNO8/Inquit/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/RYNO8/Inquit/labels{/name}', 'releases_url': 'https://api.github.com/repos/RYNO8/Inquit/releases{/id}', 'deployments_url': 'https://api.github.com/repos/RYNO8/Inquit/deployments', 'created_at': '2019-03-11T00:41:13Z', 'updated_at': '2020-01-02T08:09:34Z', 'pushed_at': '2020-01-02T08:09:33Z', 'git_url': 'git://github.com/RYNO8/Inquit.git', 'ssh_url': 'git@github.com:RYNO8/Inquit.git', 'clone_url': 'https://github.com/RYNO8/Inquit.git', 'svn_url': 'https://github.com/RYNO8/Inquit', 'homepage': 'https://ryno8.github.io/Inquit/', 'size': 70785, 'stargazers_count': 3, 'watchers_count': 3, 'language': 'Python', 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': True, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 3, 'default_branch': 'master'}, {'id': 286609159, 'node_id': 'MDEwOlJlcG9zaXRvcnkyODY2MDkxNTk=', 'name': 'OracAdditionSolve', 'full_name': 'RYNO8/OracAdditionSolve', 'private': False, 'owner': {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/RYNO8/OracAdditionSolve', 'description': None, 'fork': True, 'url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve', 'forks_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/forks', 'keys_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/teams', 'hooks_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/hooks', 'issue_events_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues/events{/number}', 'events_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/events', 'assignees_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/assignees{/user}', 'branches_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/branches{/branch}', 'tags_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/tags', 'blobs_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/languages', 'stargazers_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/stargazers', 'contributors_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/contributors', 'subscribers_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/subscribers', 'subscription_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/subscription', 'commits_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/contents/{+path}', 'compare_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/merges', 'archive_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/downloads', 'issues_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues{/number}', 'pulls_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/labels{/name}', 'releases_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/releases{/id}', 'deployments_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/deployments', 'created_at': '2020-08-11T00:43:33Z', 'updated_at': '2020-08-11T00:45:31Z', 'pushed_at': '2020-08-11T00:45:29Z', 'git_url': 'git://github.com/RYNO8/OracAdditionSolve.git', 'ssh_url': 'git@github.com:RYNO8/OracAdditionSolve.git', 'clone_url': 'https://github.com/RYNO8/OracAdditionSolve.git', 'svn_url': 'https://github.com/RYNO8/OracAdditionSolve', 'homepage': None, 'size': 6, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'Python', 'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'}]
cont = [{'login': 'Spaceghost', 'id': 251370, 'node_id': 'MDQ6VXNlcjI1MTM3MA==', 'avatar_url': 'https://avatars2.githubusercontent.com/u/251370?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/Spaceghost', 'html_url': 'https://github.com/Spaceghost', 'followers_url': 'https://api.github.com/users/Spaceghost/followers', 'following_url': 'https://api.github.com/users/Spaceghost/following{/other_user}', 'gists_url': 'https://api.github.com/users/Spaceghost/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/Spaceghost/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/Spaceghost/subscriptions', 'organizations_url': 'https://api.github.com/users/Spaceghost/orgs', 'repos_url': 'https://api.github.com/users/Spaceghost/repos', 'events_url': 'https://api.github.com/users/Spaceghost/events{/privacy}', 'received_events_url': 'https://api.github.com/users/Spaceghost/received_events', 'type': 'User', 'site_admin': False, 'contributions': 1}, {'login': 'octocat', 'id': 583231, 'node_id': 'MDQ6VXNlcjU4MzIzMQ==', 'avatar_url': 'https://avatars3.githubusercontent.com/u/583231?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/octocat', 'html_url': 'https://github.com/octocat', 'followers_url': 'https://api.github.com/users/octocat/followers', 'following_url': 'https://api.github.com/users/octocat/following{/other_user}', 'gists_url': 'https://api.github.com/users/octocat/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/octocat/subscriptions', 'organizations_url': 'https://api.github.com/users/octocat/orgs', 'repos_url': 'https://api.github.com/users/octocat/repos', 'events_url': 'https://api.github.com/users/octocat/events{/privacy}', 'received_events_url': 'https://api.github.com/users/octocat/received_events', 'type': 'User', 'site_admin': False, 'contributions': 1}]
lang = {}

# result = get_repo("contributors")
# for i in result: print(i)
#
# result = get_repo("languages", owner="aristocratos", repo="bpytop")
# print(result)
# sum = 0
# for key, value in result.items():
#     sum += value
# for key, value in result.items():
#     print(key + ":", str(round(value/sum*100, 2)) + "%")


@app.route("/bweeeah", methods=["GET", "POST"])
def index():
    form = Form()
    if request.method == "POST":
        details = request.form
        return submit(details)
    return render_template("Blair/templates/index.html", form=form)


@app.route("/submit", methods=["GET"])
def submit(form):
    if form["owner"]:
        Owner = form["owner"]
    else:
        Owner = def_owner
    if form["repo"]:
        Repo = form["repo"]
    else:
        Repo = def_repo
    print("lang", Owner, Repo)
    # lang = get_repo("languages", Owner, Repo)
    print("lang:", lang)
    print("cont", Owner, Repo)
    # cont = get_repo("contributors", Owner, Repo)
    print("cont:", cont)

    return render_template("Blair/templates/submit.html", repo=Repo, lang=lang, cont=cont, res=res)


# userList.sort(key = lambda x : x["contributions"]) # i lost the game
arryan = """social media side- using ryan's map
            languages- used, contributed, searched over time
            all repos"""


@app.route("/ryansubmit", methods=["GET"])
def ryanSync(user):
    #do magic
    return ""


if __name__ == "__main__":
    raise Exception("Don't run this file on its own. run main.py from the root directory")
