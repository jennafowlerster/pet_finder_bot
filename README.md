# pet_finder_bot

Inspiration:

This is a twitter bot by Jenna Fowler and Christine Quan that uses Petfinder.com’s API to generate a random pet that is up for adoption near Palo Alto, CA. 

While brainstorming for this bot, we knew we wanted to use pet adoption data to advertise adoptable pets, and we came across Petfinder.com, which includes information like breed, age, gender, and a photo for adoptable pets based off location. 

We thought it would be cute to create a Twitter bot to help advertise these adoptable pets, by tweeting out a random pet and its relevant information. The tweet also includes a link to a photo of the pet in the hopes that showcasing pets would increase their chances of getting adopted. 

How it Works:

This bot runs from the command line. The bot is connected to the Twitter account, PA_Pet_Finder, which refers to “Palo Alto Pet Finder” and not the beautiful state of Pennsylvania. 

Right now, the bot is set to Tweet out a random pet and their information and photo every 60 seconds, but the time between each Tweet could be adjusted. 

Again, this script and the Twitter account are Palo Alto-specific, but it wouldn’t be difficult for someone to use this script and change the location, and create their own Twitter account / application for that location. 

Process:

The hardest part of the process was probably working with the Petfinder API. Once we got the pet data, it wasn’t difficult to create a Tweet-able message, include a link to the pet’s photo, and then use Twython to Tweet from the command line. 

Conclusions:

The bot could probably be altered to be more interesting. For example, it would be useful to include the location of the shelter and a description of the shelter’s upcoming adoption events. 

Or, as Professor Nguyen suggested, it might be interesting to show how long the pet has been in its shelter to try and bring some urgency and guilt to the whole pet adoption thing. 

Future Work:

Now that we’re comfortable using Twython to send Tweets, it’ll be fun to brainstorm bots with more real-world applications. 

