import pyshorteners 
import urlexpander

# for shortener your url
def shorty(User_link):
    shorten = pyshorteners.Shortener()
    output = shorten.tinyurl.short(User_link)
    print(output)

#for expansion of shorten url

def expandy(User_link):
    expan = urlexpander.expand(User_link)
    print(expan)

#input from users
while True:
    User_link = input("Enter your link: ")
    input_for_task = input("Type 's' for shortener you url OR 'e' expansion of shortened url : ").lower()

    #for calling functions

    if input_for_task == "s":
        shorty(User_link)
    elif input_for_task == "e":
        expandy(User_link)
    
    