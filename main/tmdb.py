import requests


class TMDB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        self.session = requests.Session()

    def search(self, query):
        url = self.base_url + "/search/movie"
        params = {"api_key": self.api_key, "query": query}
        response = self.session.get(url, params=params)
        return response.json()

    def get_movie(self, movie_id):
        url = self.base_url + f"/movie/{movie_id}"
        params = {"api_key": self.api_key}
        response = self.session.get(url, params=params)
        return response.json()

# dict_keys(['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'title', 'video', 'vote_average', 'vote_count'])
TMDB = TMDB('251f099f52bc1119309cadce228f0315')
x = TMDB.search('rrr')['results'][0]
print(x.keys())
print(x)
