import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.imdb.com/list/ls057522902/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

movies = soup.find_all('div', class_='lister-item-content')

movie_data = []

for movie in movies:
    title = movie.find('h3', class_='lister-item-header').a.text.strip()
    rate = movie.find('span', class_='ipl-rating-star__rating').text.strip() if movie.find('span', class_='ipl-rating-star__rating') else 'N/A'

    # Metascore bazen olmayabilir bunun için kontrol ettim
    metascore_tag = movie.find('span', class_='metascore')
    metascore = metascore_tag.text.strip() if metascore_tag else 'N/A'
    #director oluşturma
    director_tag = movie.find('p', class_='director')
    director = movie.find('p', class_='text-muted').find('a').text.strip() if movie.find('p', class_='text-muted').find('a') else 'N/A'
    type(director)
    # Açıklama oluşturma
    description_tag = movie.find('p', class_='')
    description = description_tag.text.strip() if description_tag else 'N/A'
    #star oluşturma
    star_tag=movie.find('p' , class_= 'text-muted text-small')
    star=star_tag.text.strip() if star_tag else 'N/A'
    # Tarih oluşturma
    date_tag = movie.find('span', class_='lister-item-year text-muted unbold')
    date = date_tag.text.strip() if date_tag else 'N/A'
    type(date)
    # Link oluşturdum
    link_tag = movie.find('h3', class_='lister-item-header').a
    link = f"https://www.imdb.com{link_tag['href']}" if link_tag else 'N/A'

    # "tt" kodunu çıkarma ??
    tt_code = link.split('/')[-2]

    # yeni Link oluşturma
    new_link = f"https://www.imdb.com/title/{tt_code}/?my_argument=value"

    movie_data.append({
        'Title': title,
        'Rating': rate,
        'Metascore': metascore,
        'Director': director,
        'Description': description,
        'Date': date,
        'Link': new_link
    })

# Veri çerçevesini oluştur
df = pd.DataFrame(movie_data)

# Veriyi Excel dosyasına yaz
df.to_excel('C:\\Users\\user\\Desktop\\Kitap1.xlsx', index=False)



print(df)

pd.set_option('display.max_columns' , 500)



type(director)
