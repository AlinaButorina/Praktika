import requests
from bs4 import BeautifulSoup


def get_top_songs(artist_url):
    try:
        response = requests.get(artist_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        songs = soup.find_all("div", class_="d-track")
        artist = soup.find("h1", class_="page-artist__title").text

        if len(songs) < 10:
            print("На данном ресурсе недостаточно песен для составления топ 10 песен")
        else:
            top_songs = songs[:10]
            print(f"Топ 10 песен для исполнителя с ссылкой {artist_url}:")
            for i, song in enumerate(top_songs, 1):
                title = song.find("a", class_="d-track__title").text
                print(f"{i}. {title} - {artist}")

    except requests.HTTPError:
        print("Ошибка при запросе к веб-ресурсу")
    except requests.ConnectionError:
        print("Ошибка подключения к веб-ресурсу")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

#Мой любимый исполнитель The Weeknd, его id на площадке - 611169, поэтому в переменная artist_id должна равняться 611169
artist_id = input("Введите id исполнителя на Яндекс Музыке: ")
get_top_songs(f"https://music.yandex.ru/artist/{artist_id}/tracks")
