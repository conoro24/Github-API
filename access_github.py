
from github import Github

g = Github("7e760a69e55d4cf0c3513412d672c778b2dce87b")


for repo in g.get_user().get_repos():
    print(repo.name)
