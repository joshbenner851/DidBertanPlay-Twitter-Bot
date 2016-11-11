# -*- coding: utf-8 -*-
import Tweet
import gameScrape
from random import randint

## IMPORTANT NOTE: Twitter only allows unique tweets so this script only builds up a finite amount of unique tweets
# Therefore after this season, new emoji's and wording will be required to be able to use this next season

# Define the function that is to be executed
def my_job(text):
    twitter = Tweet.TwitterAPI()
    twitter.tweet(text)
    print("Script Triggered")

def main():
    didBertansPlay = False
    tweeted = False
    didBertansPlay = gameScrape.didPlayCurrent()
    if(didBertansPlay):
        while(not tweeted):
            try:
                # Grab a random tweet from the list
                resp = happyResponses[randint(0, (len(happyResponses)-1) )]
                happyResponses.remove(resp)
                message = resp + " #GoSpursGo"
                print("message: ", message)
                my_job(message)
                tweeted = True
            except:
                print("repeat good tweet")

    elif(didBertansPlay == False):
        while(not tweeted):
            try:
                resp = sadResponses[randint(0, (len(sadResponses)-1))]
                sadResponses.remove(resp)
                message = resp + " #GoSpursGo"
                print("message: ", message)
                my_job(message)
                tweeted = True
            except:
                print("repeat sad tweet")
    else:
        print("Script failed")


happyResponses = []
sadResponses = []

happy = ["Yes", "yes", "yup", "Mhmmm", "Aw Yeah", "Yup"]
happyEmojis = [":)", "=)", "(=", "(:", "😀", "😁", "😃", "😄" , "😆", "🙂", "😝", "😜", "👊🏻", "👌🏻", "👍🏻"]
sad = ["no", "No", "Nope", "nope", "Nah", "nah"]
sadEmjois = ["):", "=(", ":(", ")=", "🙃", "😑", "😞", "😔", "😕", "🙁"]

punctation = ["", ".", "!"]

##Create the Sad and Happy Arrays of characters because Twitter enforces a unique tweet each time.
# Also Emoji's are just more exciting to use
def createResponses():
    for x in happy:
        for y in happyEmojis:
            happyResponses.append(x + y)
        for z in punctation:
            happyResponses.append(x + z)
        happyResponses.append(x)

    for a in sad:
        for b in sadEmjois:
            sadResponses.append(a+b)
        sadResponses.append(a)

createResponses()
main()

