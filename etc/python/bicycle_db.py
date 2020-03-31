import requests
from pymongo import MongoClient



r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
rjson = r.json()


def scrap_and_insert() :
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.bikes

    def name(a):
        print(a)


    for row in rjson['rentBikeStatus']['row']:
        station = row['stationName'].split(". ")[1]
        parked = row['parkingBikeTotCnt']
        total = row['rackTotCnt']
        print(station + '(' + parked + '/' + total + ')')
        db.insert_one({'stationName': station, 'parkingBikeTotCnt': parked, 'rackTotCnt': total })

def find_and_print ():
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.bikes

    all_bikes = list(db.find())
    for bike in all_bikes:
        station = bike['stationName']
        parked = bike['parkingBikeTotCnt']
        total = bike['rackTotCnt']
        print(station + ' (' + parked + '/' + total + ')')

find_and_print()

