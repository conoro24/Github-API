

import base64
from github import Github
from pprint import pprint

username = 'conoro24'
g = Github()


def print_repo(repo):

    print("Full name:", repo.full_name)
    print("Description:", repo.description)
    print("Date created:", repo.created_at)
    print("Date of last push:", repo.pushed_at)
    print("Home Page:", repo.homepage)
    print("Language:", repo.language)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass

user = g.get_user(username)
for repo in user.get_repos():
	print_repo(repo)




