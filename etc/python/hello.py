import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
rjson = r.json()



def name(a):
    print(a)

name("시작")

for row in rjson['rentBikeStatus']['row']:
    stationName = row['stationName'].split(". ")[1]
    print(stationName + '(' + row['parkingBikeTotCnt'] + '/' +row['rackTotCnt'] + ')')

name("끝")


