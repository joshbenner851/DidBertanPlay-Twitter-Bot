# -*- coding: utf-8 -*-
import Tweet
import gameScrape


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

                message = happyResponses.pop() + " #GoSpursGo"
                print("message: ", message)
                my_job(message)
                tweeted = True
            except:
                print("repeat good tweet")

    elif(didBertansPlay == False):
        while(not tweeted):
            try:
                message = sadResponses.pop() + " #GoSpursGo"
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
#print(happyResponses)
#print(len(happyResponses))
print()
#print(sadResponses)
#print(len(sadResponses))

main()

