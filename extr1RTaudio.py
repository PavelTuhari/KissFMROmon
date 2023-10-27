import requests
from bs4 import BeautifulSoup
import time

def get_song_name():
    response = requests.get('https://www.kissfm.ro/')
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find('h2', class_='aw-top-now-playing-trackname')
    
    if element:
        return element.text.strip()
    return None

previous_song = ""
while True:
    current_song = get_song_name()
    if current_song and current_song != previous_song:
        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{current_song}"
        
        # Запись в файл
        with open('log.txt', 'a') as file:
            file.write(log_entry + "\n")
        
        # Вывод на экран
        print(log_entry)
        
        previous_song = current_song
    time.sleep(30)
