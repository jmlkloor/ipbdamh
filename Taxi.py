import pandas as pd
from time import time
import requests
import shutil
import os.path
from bson import ObjectId
from pymongo import MongoClient
import sys
import gridfs
import json

def inladen():
    begin = time()
    jaar = 19
    jaartal = '%02d' % jaar
    maand = 12
    maandtal = '%02d' % maand

    if os.path.exists(r"C:\Users\Kevin\Desktop\Data\Opslag2.txt"):
        list1 = []
        with open(r"C:\Users\Kevin\Desktop\Data\Opslag2.txt") as file:
            for line in file:
                list1.append(line)
        jaar = int(list1[0])
        maand = int(list1[1])
        while jaartal != "100":
            jaartal = '%02d' % jaar
            maandtal = '%02d' % maand
            if maandtal == "12":
                data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal,maandtal), low_memory=False)
                client = MongoClient("mongodb://localhost:27017/")
                db = client["API"]
                datacsv = data.to_csv()
                fs = gridfs.GridFS(db)
                fs.put(datacsv, encoding="UTF-8")
                maand = 1
                jaar = jaar + 1
                del data
            else:
                client = MongoClient("mongodb://localhost:27017/")
                db = client["API"]
                try:
                    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal, maandtal),low_memory=False)
                    datacsv = data.to_csv()
                    fs = gridfs.GridFS(db)
                    fs.put(datacsv, encoding="UTF-8")
                    del data
                except Exception as e:
                    print("Failure!!")
                    print(e)
                    maken = open(r"C:\Users\Kevin\Desktop\Data\Opslag2.txt", "w")
                    maken.write(str(jaar) + "\n")
                    maken.write(str(maand) + "\n")
                    maken.close()
                    return
                maand = maand + 1
                maandtal = '%02d' % maand
                print(jaartal, maandtal)

    else:
        while jaartal != "100":
            if maandtal == "12":
                print("Het inladen van de data begint nu")
                client = MongoClient("mongodb://localhost:27017/")
                db = client["API"]
                data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal, maandtal),low_memory=False)
                datacsv = data.to_csv()
                fs = gridfs.GridFS(db)
                fs.put(datacsv, encoding="UTF-8")
                maand = 1
                jaar = jaar + 1
                maandtal = '%02d' % maand
                jaartal = '%02d' % jaar
                del data
            else:
                client = MongoClient("mongodb://localhost:27017/")
                db = client["API"]
                try:
                    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal, maandtal),low_memory=False)
                    print("Het inladen van de data begint nu")
                    datacsv = data.to_csv()
                    fs = gridfs.GridFS(db)
                    fs.put(datacsv, encoding="UTF-8")
                    del data
                except Exception as e:
                    print(e)
                    print("Failure!!")
                    maken = open(r"C:\Users\Kevin\Desktop\Data\Opslag2.txt", "w")
                    maken.write(str(jaar) + "\n")
                    maken.write(str(maand) + "\n")
                    maken.close()
                    eind = time()
                    tijd = (eind - begin)
                    print(round(tijd), "seconden")
                    return
                maand = maand + 1
                maandtal = '%02d' % maand
                print(jaartal, maandtal)
    eind = time()
    tijd = (eind - begin)
    print(round(tijd), "seconden")

def performancetest():
    print("Hoeveel megabyte wilt u inladen?")
    mb = int(input())
    mb = mb * 2500
    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File1.csv",low_memory=False,nrows=mb)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["API"]
    a = sys.getsizeof(data)
    a = a / 1000000
    print(round(a),"mb")
    datacsv = data.to_csv()
    fs = gridfs.GridFS(db)
    fs.put(datacsv,encoding="UTF-8")

def query():
    begin = time()
    print("het ophalen van de data begint")

    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File1912.csv", low_memory=False)
    pd.set_option('display.max_columns', None)
    print(data.shape)
    print(data.info())
    print(data.head())
    print(data.describe())

    #print(pd.crosstab(data['vendor_name'],['Payment_Type'], margins=True))

    eind = time()
    tijd = (eind - begin)
    print(round(tijd), "seconden")


def bestanden():
    begin = time()

    jaar = 19
    jaartal = '%02d' % jaar
    maand = 12
    maandtal = '%02d' % maand

    if os.path.exists(r"C:\Users\Kevin\Desktop\Data\Opslag.txt"):
        list1 = []
        with open(r"C:\Users\Kevin\Desktop\Data\Opslag.txt") as file:
            for line in file:
                list1.append(line)
        jaar = int(list1[0])
        maand = int(list1[1])
        jaartal = '%02d' % jaar
        maandtal = '%02d' % maand
        while jaartal != "100":
            if maandtal == "12":
                url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_20{}-{}.csv".format(jaartal, maandtal)
                r = requests.get(url, verify=False, stream=True)
                r.raw.decode_content = True
                with open(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal,maandtal), 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print("Success")
                maand = 1
                jaar = jaar + 1
                maandtal = '%02d' % maand
                jaartal = '%02d' % jaar
            else:
                url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_20{}-{}.csv".format(jaartal,maandtal)
                r = requests.get(url, verify=False, stream=True)
                if r.status_code != 200:
                    print("Failure!!")
                    maken = open(r"C:\Users\Kevin\Desktop\Data\Opslag.txt", "w")
                    maken.write(str(jaar) + "\n")
                    maken.write(str(maand) + "\n")
                    maken.close()
                    return
                else:
                    r.raw.decode_content = True
                    with open(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal,maandtal), 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    print("Success")
                maand = maand + 1
                maandtal = '%02d' % maand
                print(jaartal, maandtal)

    else:
        while jaartal != "100":
            if maandtal == "12":
                url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_20{}-{}.csv".format(jaartal, maandtal)
                r = requests.get(url, verify=False, stream=True)
                r.raw.decode_content = True
                with open(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal,maandtal), 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print("Success")
                maand = 1
                jaar = jaar + 1
                maandtal = '%02d' % maand
                jaartal = '%02d' % jaar
            else:
                url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_20{}-{}.csv".format(jaartal,maandtal)
                r = requests.get(url, verify=False, stream=True)
                if r.status_code != 200:
                    print("Failure!!")
                    maken = open(r"C:\Users\Kevin\Desktop\Data\Opslag.txt", "w")
                    maken.write(str(jaar) + "\n")
                    maken.write(str(maand) + "\n")
                    maken.close()
                    return
                else:
                    r.raw.decode_content = True
                    with open(r"C:\Users\Kevin\Desktop\Data\File{}{}.csv".format(jaartal,maandtal), 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    print("Success")
                maand = maand + 1
                maandtal = '%02d' % maand
                print(jaartal, maandtal)

    eind = time()
    tijd = (eind - begin)
    print(round(tijd), "seconden")


if __name__ == '__main__':
    #bestanden()
    inladen()

    query()

    #performancetest()

