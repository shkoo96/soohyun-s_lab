import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
lists = soup.select('tbody > tr')
rank= 0

for list in lists:
    title = list.select_one('a')
    rate = list.select_one('td.point')
    if title is not None:
        rank += 1
        print(rank, title.text, rate.text)
