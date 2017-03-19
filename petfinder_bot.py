import petfinder
from petfinder.client import PetFinderClient
import requests
import rauth
import pprint

api_key = "08ef4349bcc1d9a7e81a869195ff3a9f"
api_secret = "e0d8a6b6bfdee081e5fd8982e1057aa3"

API_URL= "http://api.petfinder.com/pet.get"
API_GET_RANDOM = "http://api.petfinder.com/pet.getRandom"

def get_random_params(location):

    params = dict()
    params["key"] = api_key
    params["format"] = "json"
    params["location"] = location

    return params

def get_params(petid):
    params = dict()
    params["key"] = api_key
    params['id'] = petid
    params["format"] = "json"
    return params

def query_API(API_URL, params):

    resp = requests.get(API_URL, params = params)
    data = resp.json()

    return data

location = "Palo Alto, CA"

params = get_random_params(location)
randompetID = int(query_API(API_GET_RANDOM, params)['petfinder']['petIds']['id']['$t'])
new_params = get_params(randompetID)
data = query_API(API_URL, new_params)

def make_story(data):
    description = data['petfinder']['pet']['description']['$t']
    pic = data['petfinder']['pet']['media']['photos']['photo'][0]['$t']

    return description + pic

print(make_story(data))
