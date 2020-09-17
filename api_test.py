import requests

def movie_req(name):
    r = requests.get("http://www.omdbapi.com/", params={"t": name, "apikey": "9f6d550c"})
    return r.json()
