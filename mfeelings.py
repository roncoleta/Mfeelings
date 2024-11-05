import requests
import random

# Chave de API do Last.fm
API_KEY = '2b41f7dcc9678e94e18f7b3b017bcd61'
BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

# Função para buscar álbuns populares em um gênero específico
def fetch_albums_by_genre(genre):
    params = {
        'method': 'tag.gettopalbums',
        'tag': genre,
        'api_key': API_KEY,
        'format': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        albums = response.json()['albums']['album']
        album_list = [f"{album['name']} - {album['artist']['name']}" for album in albums]
        return album_list
    else:
        print("Erro ao buscar dados da API.")
        return []

# Função para recomendar álbuns com base no gênero e na emoção
def recommend_album(emotion, genre):
    albums = fetch_albums_by_genre(genre)
    if albums:
        recommended_album = random.choice(albums)
        return recommended_album
    else:
        return "Infelizmente, não encontramos álbuns para o gênero escolhido."

# Função principal
def main():
    emotion = input("Escolha uma emoção (alegria, tristeza, energia, calma): ").lower()
    genre = input("Escolha um gênero musical (rap, rock, pop): ").lower()
    album = recommend_album(emotion, genre)
    
    print(f"Essa é a call: {album}")
    
main()


