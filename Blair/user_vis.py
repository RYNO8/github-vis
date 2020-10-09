#### TODO ####
# implement user visualisation from url: /users?user=[username here]
# find a better url name on line 54 (you cant have it at "/")

#links:
#parameter passing in urls: https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask

from flask import Flask, render_template, request, jsonify
import requests
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from form1 import Form
import json
import webbrowser
import github

# Pie chart imports
from math import pi
from bokeh.transform import cumsum
from bokeh.plotting import figure, ColumnDataSource
from bokeh.embed import components
from bokeh.palettes import Turbo256


app = Flask(__name__)
app.secret_key = "super secret"
bootstrap = Bootstrap(app)
# g = github.Github("test-user1337", "cyrilhas2iq")
# print(g.get_user())


auth = ("my_client_id", "")
def_owner = "octocat"
def_repo = "hello-world"
others = [("indy256", "codejam-templates"), ("NZIO", "nztrain")]
def_header = {"Accept": "application/vnd.github.v3+json"}



def get_user(url="", user=def_owner, headers=def_header):
    result = requests.get(f"https://api.github.com/users/{user}{url}", headers=headers).json()
    return result


def get_repo(url, owner=def_owner, repo=def_repo, headers=def_header):
    result = requests.get(f"https://api.github.com/repos/{owner}/{repo}/{url}", headers=headers).json()
    return result


user_info = {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': 'I LOST THE GAME', 'twitter_username': None, 'public_repos': 3, 'public_gists': 0, 'followers': 16, 'following': 32, 'created_at': '2018-01-10T03:32:51Z', 'updated_at': '2020-08-24T10:53:24Z'}
# get_user(user="ryno8")
res = [{'id': 174899437, 'node_id': 'MDEwOlJlcG9zaXRvcnkxNzQ4OTk0Mzc=', 'name': 'Inquit', 'full_name': 'RYNO8/Inquit', 'private': False, 'owner': {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/RYNO8/Inquit', 'description': 'An unblocked messaging app', 'fork': False, 'url': 'https://api.github.com/repos/RYNO8/Inquit', 'forks_url': 'https://api.github.com/repos/RYNO8/Inquit/forks', 'keys_url': 'https://api.github.com/repos/RYNO8/Inquit/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/RYNO8/Inquit/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/RYNO8/Inquit/teams', 'hooks_url': 'https://api.github.com/repos/RYNO8/Inquit/hooks', 'issue_events_url': 'https://api.github.com/repos/RYNO8/Inquit/issues/events{/number}', 'events_url': 'https://api.github.com/repos/RYNO8/Inquit/events', 'assignees_url': 'https://api.github.com/repos/RYNO8/Inquit/assignees{/user}', 'branches_url': 'https://api.github.com/repos/RYNO8/Inquit/branches{/branch}', 'tags_url': 'https://api.github.com/repos/RYNO8/Inquit/tags', 'blobs_url': 'https://api.github.com/repos/RYNO8/Inquit/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/RYNO8/Inquit/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/RYNO8/Inquit/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/RYNO8/Inquit/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/RYNO8/Inquit/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/RYNO8/Inquit/languages', 'stargazers_url': 'https://api.github.com/repos/RYNO8/Inquit/stargazers', 'contributors_url': 'https://api.github.com/repos/RYNO8/Inquit/contributors', 'subscribers_url': 'https://api.github.com/repos/RYNO8/Inquit/subscribers', 'subscription_url': 'https://api.github.com/repos/RYNO8/Inquit/subscription', 'commits_url': 'https://api.github.com/repos/RYNO8/Inquit/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/RYNO8/Inquit/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/RYNO8/Inquit/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/RYNO8/Inquit/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/RYNO8/Inquit/contents/{+path}', 'compare_url': 'https://api.github.com/repos/RYNO8/Inquit/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/RYNO8/Inquit/merges', 'archive_url': 'https://api.github.com/repos/RYNO8/Inquit/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/RYNO8/Inquit/downloads', 'issues_url': 'https://api.github.com/repos/RYNO8/Inquit/issues{/number}', 'pulls_url': 'https://api.github.com/repos/RYNO8/Inquit/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/RYNO8/Inquit/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/RYNO8/Inquit/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/RYNO8/Inquit/labels{/name}', 'releases_url': 'https://api.github.com/repos/RYNO8/Inquit/releases{/id}', 'deployments_url': 'https://api.github.com/repos/RYNO8/Inquit/deployments', 'created_at': '2019-03-11T00:41:13Z', 'updated_at': '2020-01-02T08:09:34Z', 'pushed_at': '2020-01-02T08:09:33Z', 'git_url': 'git://github.com/RYNO8/Inquit.git', 'ssh_url': 'git@github.com:RYNO8/Inquit.git', 'clone_url': 'https://github.com/RYNO8/Inquit.git', 'svn_url': 'https://github.com/RYNO8/Inquit', 'homepage': 'https://ryno8.github.io/Inquit/', 'size': 70785, 'stargazers_count': 3, 'watchers_count': 3, 'language': 'Python', 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': True, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 3, 'default_branch': 'master'}, {'id': 289902353, 'node_id': 'MDEwOlJlcG9zaXRvcnkyODk5MDIzNTM=', 'name': 'onecore', 'full_name': 'RYNO8/onecore', 'private': False, 'owner': {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/RYNO8/onecore', 'description': None, 'fork': True, 'url': 'https://api.github.com/repos/RYNO8/onecore', 'forks_url': 'https://api.github.com/repos/RYNO8/onecore/forks', 'keys_url': 'https://api.github.com/repos/RYNO8/onecore/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/RYNO8/onecore/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/RYNO8/onecore/teams', 'hooks_url': 'https://api.github.com/repos/RYNO8/onecore/hooks', 'issue_events_url': 'https://api.github.com/repos/RYNO8/onecore/issues/events{/number}', 'events_url': 'https://api.github.com/repos/RYNO8/onecore/events', 'assignees_url': 'https://api.github.com/repos/RYNO8/onecore/assignees{/user}', 'branches_url': 'https://api.github.com/repos/RYNO8/onecore/branches{/branch}', 'tags_url': 'https://api.github.com/repos/RYNO8/onecore/tags', 'blobs_url': 'https://api.github.com/repos/RYNO8/onecore/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/RYNO8/onecore/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/RYNO8/onecore/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/RYNO8/onecore/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/RYNO8/onecore/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/RYNO8/onecore/languages', 'stargazers_url': 'https://api.github.com/repos/RYNO8/onecore/stargazers', 'contributors_url': 'https://api.github.com/repos/RYNO8/onecore/contributors', 'subscribers_url': 'https://api.github.com/repos/RYNO8/onecore/subscribers', 'subscription_url': 'https://api.github.com/repos/RYNO8/onecore/subscription', 'commits_url': 'https://api.github.com/repos/RYNO8/onecore/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/RYNO8/onecore/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/RYNO8/onecore/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/RYNO8/onecore/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/RYNO8/onecore/contents/{+path}', 'compare_url': 'https://api.github.com/repos/RYNO8/onecore/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/RYNO8/onecore/merges', 'archive_url': 'https://api.github.com/repos/RYNO8/onecore/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/RYNO8/onecore/downloads', 'issues_url': 'https://api.github.com/repos/RYNO8/onecore/issues{/number}', 'pulls_url': 'https://api.github.com/repos/RYNO8/onecore/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/RYNO8/onecore/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/RYNO8/onecore/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/RYNO8/onecore/labels{/name}', 'releases_url': 'https://api.github.com/repos/RYNO8/onecore/releases{/id}', 'deployments_url': 'https://api.github.com/repos/RYNO8/onecore/deployments', 'created_at': '2020-08-24T10:53:33Z', 'updated_at': '2020-08-25T07:02:12Z', 'pushed_at': '2020-08-25T07:02:10Z', 'git_url': 'git://github.com/RYNO8/onecore.git', 'ssh_url': 'git@github.com:RYNO8/onecore.git', 'clone_url': 'https://github.com/RYNO8/onecore.git', 'svn_url': 'https://github.com/RYNO8/onecore', 'homepage': None, 'size': 4932, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'HTML', 'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'}, {'id': 286609159, 'node_id': 'MDEwOlJlcG9zaXRvcnkyODY2MDkxNTk=', 'name': 'OracAdditionSolve', 'full_name': 'RYNO8/OracAdditionSolve', 'private': False, 'owner': {'login': 'RYNO8', 'id': 35283610, 'node_id': 'MDQ6VXNlcjM1MjgzNjEw', 'avatar_url': 'https://avatars3.githubusercontent.com/u/35283610?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/RYNO8', 'html_url': 'https://github.com/RYNO8', 'followers_url': 'https://api.github.com/users/RYNO8/followers', 'following_url': 'https://api.github.com/users/RYNO8/following{/other_user}', 'gists_url': 'https://api.github.com/users/RYNO8/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/RYNO8/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/RYNO8/subscriptions', 'organizations_url': 'https://api.github.com/users/RYNO8/orgs', 'repos_url': 'https://api.github.com/users/RYNO8/repos', 'events_url': 'https://api.github.com/users/RYNO8/events{/privacy}', 'received_events_url': 'https://api.github.com/users/RYNO8/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/RYNO8/OracAdditionSolve', 'description': None, 'fork': True, 'url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve', 'forks_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/forks', 'keys_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/teams', 'hooks_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/hooks', 'issue_events_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues/events{/number}', 'events_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/events', 'assignees_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/assignees{/user}', 'branches_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/branches{/branch}', 'tags_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/tags', 'blobs_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/languages', 'stargazers_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/stargazers', 'contributors_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/contributors', 'subscribers_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/subscribers', 'subscription_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/subscription', 'commits_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/contents/{+path}', 'compare_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/merges', 'archive_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/downloads', 'issues_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/issues{/number}', 'pulls_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/labels{/name}', 'releases_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/releases{/id}', 'deployments_url': 'https://api.github.com/repos/RYNO8/OracAdditionSolve/deployments', 'created_at': '2020-08-11T00:43:33Z', 'updated_at': '2020-08-11T00:45:31Z', 'pushed_at': '2020-08-11T00:45:29Z', 'git_url': 'git://github.com/RYNO8/OracAdditionSolve.git', 'ssh_url': 'git@github.com:RYNO8/OracAdditionSolve.git', 'clone_url': 'https://github.com/RYNO8/OracAdditionSolve.git', 'svn_url': 'https://github.com/RYNO8/OracAdditionSolve', 'homepage': None, 'size': 6, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'Python', 'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'}]
# get_user("/repos", "ryno8")
cont = [{'login': 'Spaceghost', 'id': 251370, 'node_id': 'MDQ6VXNlcjI1MTM3MA==', 'avatar_url': 'https://avatars2.githubusercontent.com/u/251370?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/Spaceghost', 'html_url': 'https://github.com/Spaceghost', 'followers_url': 'https://api.github.com/users/Spaceghost/followers', 'following_url': 'https://api.github.com/users/Spaceghost/following{/other_user}', 'gists_url': 'https://api.github.com/users/Spaceghost/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/Spaceghost/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/Spaceghost/subscriptions', 'organizations_url': 'https://api.github.com/users/Spaceghost/orgs', 'repos_url': 'https://api.github.com/users/Spaceghost/repos', 'events_url': 'https://api.github.com/users/Spaceghost/events{/privacy}', 'received_events_url': 'https://api.github.com/users/Spaceghost/received_events', 'type': 'User', 'site_admin': False, 'contributions': 1}, {'login': 'octocat', 'id': 583231, 'node_id': 'MDQ6VXNlcjU4MzIzMQ==', 'avatar_url': 'https://avatars3.githubusercontent.com/u/583231?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/octocat', 'html_url': 'https://github.com/octocat', 'followers_url': 'https://api.github.com/users/octocat/followers', 'following_url': 'https://api.github.com/users/octocat/following{/other_user}', 'gists_url': 'https://api.github.com/users/octocat/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/octocat/subscriptions', 'organizations_url': 'https://api.github.com/users/octocat/orgs', 'repos_url': 'https://api.github.com/users/octocat/repos', 'events_url': 'https://api.github.com/users/octocat/events{/privacy}', 'received_events_url': 'https://api.github.com/users/octocat/received_events', 'type': 'User', 'site_admin': False, 'contributions': 1}]
# get_repo("/languages")
lang = {}
# lang = requests.get(f"https://api.github.com/repos/{others[0][0]}/{others[0][1]}/languages", headers=def_header).json()
# get_repo("/contributions")
# commits = requests.get(f"https://api.github.com/repos/ryno8/inquit/commits", headers=def_header).json()



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


@app.route("/", methods=["GET", "POST"])
def index():
    form = Form()
    if request.method == "POST":
        details = request.form
        return "hello world! ur using the wrong path"
    return render_template("index.html", form=form)


# userList.sort(key = lambda x : x["stargazers_count"], reverse = true) # i lost the game
arryan = """social media side- using ryan's map
            languages- used, contributed, searched over time
            all repos"""
ryno = """fav lang function"""


def fav_lang(repo):
    langs = get_repo("languages", owner=repo["owner"]["login"], repo=repo["name"])
    FavLang = ""
    uses = 0
    for key, val in langs.items():
        if val > uses:
            FavLang = key
            uses = val
    return FavLang


@app.route("/ryansubmit", methods=["GET"])
def ryanSync():
    user = request.args.get("user")
    if not user:
        print("no user")
        user = "RYNO8"
    print(user)
    User_info = get_user(user=user)
    User_repos = get_user("/repos", user)
    User_repos.sort(key=lambda x: x["stargazers_count"], reverse=True) #most stargazers come first
    favlang = "None"
    if len(User_repos) > 0:
        favLang = fav_lang(User_repos[0])
    print(User_info)
    print(User_repos)
    # print(res)
    # print(user_info)
    return render_template("submit.html", res=User_repos, user_info=User_info, favLang=favLang)


def pi_chart(result): #ronalds part
    sum = 0
    languages = []
    percentages = []
    angles = []
    palette = ["#000000", "#00009C", "#00BFFF", "#00AF33", "#551011",
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
            line_color="white", fill_color='colours', legend_field='languages', source=source)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    p.outline_line_color = None

    return components(p)


@app.route("/ronaldsubmit", methods=["GET"])
def ronaldSync():
    Owner = request.args.get("owner")
    Repo = request.args.get("repo")
    result = get_repo("languages", owner=Owner, repo=Repo)
    print("result", result)
    pi_script, pi_div = pi_chart(result)

    return render_template("ronaldsubmit.html", pi_script=pi_script, pi_div=pi_div)


if __name__ == "__main__":
    app.run()
