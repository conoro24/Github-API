
import requests
from pprint import pprint

username = 'conoro24'
url = 'https://api.github.com/users/conoro24'

user_data = requests.get(url).json()
pprint(user_data)


