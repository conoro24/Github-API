
import base64
from github import Github
from pprint import pprint

username = 'conoro24'
g = Github()

user = g.get_user(username)
for repo in user.get_repos():
	pprint(repo)





