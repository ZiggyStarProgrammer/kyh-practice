import requests
from pprint import pprint


def main():
    movie_name = input("Vad vill du se för film?")
    movie = movie_req(name=movie_name)
    print(f"***Resultat från OMDB!***\n{movie['Title']} ({movie['Year']}) Regisserades av {movie['Director']} \n"
          f"Skådisar: {movie['Actors']} \nIMDB betyg: {movie['imdbRating']} \n"
          f"Awards: {movie['Awards']} \nLängd: {movie['Runtime']}")


def movie_req(name):
    d = {"t": name, "apikey": "9f6d550c"}
    r = requests.get("http://www.omdbapi.com/", params=d)
    return r.json()


if __name__ == '__main__':
    main()
