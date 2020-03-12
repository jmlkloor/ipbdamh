import pandas as pd
from time import time
import requests
import shutil
from pymongo import MongoClient
import sys

begin = time()
def callme():
    url = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2009-01.csv"
    r = requests.get(url, verify=False,stream=True)
    if r.status_code!=200:
        print( "Failure!!")
        exit()
    else:
        r.raw.decode_content = True
        with open("file1.csv", 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print( "Success")

def databaseschrijven():
    data = pd.read_csv(r"C:\Users\Kevin\Desktop\Data\File1.csv",low_memory=False,nrows=100000)
    client = MongoClient("mongodb://localhost:27017/")
    # Hier wordt duidelijk gemaakt met welke database er connectie moet worden gemaakt
    db = client["API"]
    # Hier wordt duidelijk gemaakt met welke collectie er connectie moet worden gemaakt
    collection = db["APIcollection"]
    a = sys.getsizeof(data)
    a = a / 1000000
    print(round(a),"mb")
    #datadict = data.to_dict('records')
    #collection.insert_one({"Data" : datadict})

if __name__ == '__main__':
    #callme()
    databaseschrijven()


eind = time()
tijd = (eind - begin)
print(tijd)
