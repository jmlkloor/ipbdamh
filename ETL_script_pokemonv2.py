from pymongo import MongoClient
import requests

# Binnen deze functie staan de database gegevens die nodig zijn
def databasegegevens():
    # Hier wordt de database connectie gegevens opgeslagen in een variabelen
    client = MongoClient("mongodb+srv://jmlkloor:shira001@ipbdamh-xjb09.azure.mongodb.net/test?retryWrites=true&w=majority")
    #client = MongoClient("mongodb://localhost:27017/")
    # Hier wordt duidelijk gemaakt met welke database er connectie moet worden gemaakt
    db = client["API"]
    # Hier wordt duidelijk gemaakt met welke collectie er connectie moet worden gemaakt
    collection = db["APIcollection"]
    # hier wordt de collection teruggegeven zodat ik het verder in de code kan gebruiken
    return collection


# Binnen deze functie wordt het ETL proces gehandeld
def ETL(collection):
    # Deze variabele bevat de pokemon API
    pokemonAPI = "https://pokeapi.co/api/v2/pokemon?limit=807"
    # Hier wordt de data uit de pokemonAPI gehaald en aan een variabele gekoppeld
    pokemonAPIdata = requests.get(url=pokemonAPI)
    # Hier wordt de rauwe api data omgezet naar een json structuur
    pokemonAPIjson = pokemonAPIdata.json()
    # hier wordt een lijst aangemaakt die later wordt gebruikt in de while loop
    databaselist = []
    # hier wordt een teller gemaakt die gebruikt wordt voor de while loop
    teller = 0
    # Met deze while loop wordt er door de json data heen gegaan
    while teller < 807:
        # Hier wordt de data uit de json structuur gehaald en in een dictionary gezet
        pokemondict = {"naam": pokemonAPIjson['results'][teller]['name'],"url": pokemonAPIjson['results'][teller]['url']}
        # Hier wordt de URL gehaald uit de dictionary zodat ik de rest van de pokemon attributet kan ophalen
        pokemonattr = pokemondict.get('url')
        # hier wordt de url gebruikt om de pokemon attributen op te halen
        pokemonattrAPI = requests.get(url=pokemonattr)
        # hier wordt de opgehaalde data omgezet in een json structuur
        pokemonattrjsonAPI = pokemonattrAPI.json()

        #Deze onderstaande statements zorgen ervoor dat de attributen die niet nodig zijn worden verwijderd
        del pokemonattrjsonAPI["held_items"]
        del pokemonattrjsonAPI["abilities"]
        del pokemonattrjsonAPI["base_experience"]
        del pokemonattrjsonAPI["forms"]
        del pokemonattrjsonAPI["game_indices"]
        del pokemonattrjsonAPI["height"]
        del pokemonattrjsonAPI["is_default"]
        del pokemonattrjsonAPI["location_area_encounters"]
        del pokemonattrjsonAPI["moves"]
        del pokemonattrjsonAPI["species"]
        del pokemonattrjsonAPI["sprites"]
        del pokemonattrjsonAPI["stats"]
        del pokemonattrjsonAPI["weight"]

        # Hier wordt de dictionary gemaakt die aan de lijst hieronder wordt toegevoegd
        lijstdict = {"naam": pokemonAPIjson['results'][teller]['name'], "attr": pokemonattrjsonAPI}
        # hier wordt de dictionary toegoegd aan de lijst
        databaselist.append(lijstdict)
        # hier wordt de teller met 1 verhoogd zodat de volgende pokemon kan worden toegevoegd
        teller = teller + 1
    # Hier wordt de data in de mongoDB geladen
    collection.insert_one({"data": databaselist})

# hier worden de functie die zijn aangemaakt gebruikt
if __name__ == "__main__":
    # Hier wordt de databasegegevens aan een variabele gekoppeld
    collection = databasegegevens()
    ETL(collection)
