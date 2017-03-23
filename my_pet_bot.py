import requests
from twython import Twython
import json
from time import sleep

def get_pet_params(location):

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

def make_story(data):
    description = data['petfinder']['pet']['description']['$t']
    name = data['petfinder']['pet']['name']['$t']
    age = data['petfinder']['pet']['age']['$t']
    animal_type = data['petfinder']['pet']['animal']['$t']
    sex = data['petfinder']['pet']['sex']['$t']
    pic = data['petfinder']['pet']['media']['photos']['photo'][0]['$t']

    return "Hello, my name is {name}. My age is {age}. I am a {animal_type}. My gender is {sex}. {pic}".format(name=name, age=age, animal_type=animal_type, sex=sex, pic=pic)


CREDENTIALS_FILENAME = 'creds-twitter-bot.json'
jf = open(CREDENTIALS_FILENAME)
creds = json.load(jf)
jf.close()

client = Twython(creds['consumer_key'],
                  creds['consumer_secret'],
                  creds['access_token'],
                  creds['access_token_secret'])

results = client.search(q='"PA_Pet_Finder"', count=100, result_type="recent")
tweets = results['statuses']

api_key = "08ef4349bcc1d9a7e81a869195ff3a9f"
api_secret = "e0d8a6b6bfdee081e5fd8982e1057aa3"

API_URL= "http://api.petfinder.com/pet.get"
API_GET_RANDOM = "http://api.petfinder.com/pet.getRandom"

location = "Palo Alto, CA"

pet_params = get_pet_params(location)

#print(tweet_text)
#client.update_status(status=tweet_text) #, in_reply_to_status_id=tweet_id)
while True:
    randompetID = int(query_API(API_GET_RANDOM, pet_params)['petfinder']['petIds']['id']['$t'])
    new_params = get_params(randompetID)
    data = query_API(API_URL, new_params)
    tweet_text = make_story(data)
    print(tweet_text)
    client.update_status(status=tweet_text)
    sleep(60)
    #can change to 60 * 60 * 24 to tweet daily instead of every minute
