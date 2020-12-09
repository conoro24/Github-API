
from github import Github

g = Github("a343260157823bdbf95311f60966c2ca8b638ea5")


for repo in g.get_user().get_repos():
    print(repo.name)