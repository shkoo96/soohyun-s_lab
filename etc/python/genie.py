import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

lists = soup.select('tr.list')
for list in lists:
    songName = list.select_one('a.title').text.strip()
    singerName = list.select_one('a.artist').text.strip()
    ranking = list.select_one('td.number').text.strip().split(' ')[0].strip()
    print('[' + ranking + '] ' + songName + '/ ' + singerName)












