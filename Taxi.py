import pandas as pd
import numpy as np
from time import time
import requests
import shutil
from pymongo import MongoClient
import sys
import gridfs

begin = time()
def callme():
    url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2009-01.csv"
    r = requests.get(url, verify=False,stream=True)
    if r.status_code!=200:
        print( "Failure!!")
        exit()
    else:
        r.raw.decode_content = True
        with open(r"C:\Users\Kevin\Desktop\Data\File1.csv", 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print( "Success")

def databaseschrijven():
    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File1.csv",low_memory=False)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["API"]
    a = sys.getsizeof(data)
    a = a / 1000000
    print(round(a),"mb")
    datacsv = data.to_csv()
    fs = gridfs.GridFS(db)
    fs.put(datacsv,encoding="utf-8")

def test():
    shepherd = "Mary"
    age = 32
    stuff_in_string = "Shepherd {} is {} years old.".format(shepherd, age)
    print(stuff_in_string)

def test2():
    jaar = 9
    jaartal = '%02d' % jaar
    maand = 0
    maandtal = '%02d' % maand

    while jaartal != "11":
        if maandtal == "12":
            maand = 0
            jaar = jaar + 1
            maandtal = '%02d' % maand
            jaartal = '%02d' % jaar
        else:
            maand = maand + 1
            maandtal = '%02d' % maand
            print(jaartal,maandtal)


        #als er dan bij de if inplaats van exit moet hij eerst de laatste combinatie opslaan en dan deze weer terughalen.



    #url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2009-01.csv"
    #r = requests.get(url, verify=False, stream=True)
    #if r.status_code!=200:
    #    print( "Failure!!")
    #    exit()
    #else:
    #    r.raw.decode_content = True
    #    with open(r"C:\Users\Kevin\Desktop\Data\File1.csv", 'wb') as f:
    #        shutil.copyfileobj(r.raw, f)
    #    print( "Success")


if __name__ == '__main__':
    #callme()
    #databaseschrijven()
    #test()
    test2()


eind = time()
tijd = (eind - begin)
print(round(tijd),"seconden")
