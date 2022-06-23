#Application that has a GUI that allows the user to look up trends and then search for the most popular tweets
#should allow the user to search for tweets with specific hashtags
#Author: Joshua Ellis
#Not for commercial use!


import tweepy

from Encry.cryp import encrypt, decryp


class scrap:
    def __init__(self, hashT, number):
        self.hashT = hashT
        self.number = number


    #function to search twitter for tweets containing the hashtag
    def scraper(self):
            
            
            file_path = decryp()
            all_keys = open(file_path, 'r').read().splitlines()
            api_key = all_keys[0]
            api_key_sec = all_keys[1]
            access_Tok = all_keys[2]
            access_Tok_sec = all_keys[3]

            auth = tweepy.OAuthHandler(api_key, api_key_sec)
            auth.set_access_token(access_Tok, access_Tok_sec)

            api = tweepy.API(auth)

            # iterator to show which tweet it is
            i = 1

            # gets tweets that contain the requested hashtag, sorted by likes and english only, into a iterable object
            tweets = tweepy.Cursor(api.search, q=self.hashT, result_type='popular', lang='en',
            tweet_mode='extended').items(self.number)

            #list comprehension: goes through the iterable object and adds the tweet to the list
            #Twitter_List = [tweet for tweet in tweets]
            Twitter_List = []
            for tweet in tweets:
                Twitter_List.append(tweet)
            
            iTweet = "" 
            #goes through every tweet in the list and splits the content into variables
            for tweet in Twitter_List:
                username = tweet.user.screen_name #gets the name of the user
                hashtags = tweet.entities['hashtags'] #finds the hashtags used in the current tweet
                text = tweet.full_text #gets the actual text of the tweet

                #makes an empty list
                hashtext = ""
                #print(hashtags)
                #appends the hashtags used in the current tweet to the list
                for x in range(len(hashtags)):
                    hashtext += hashtags[x]['text']
                   
                
                #create one big string containing the information
                iTweet += "\n------------------------------\n" + "Tweet " + str(i) + ":" + "\n" + "Username: " + username + "\n"  + "Text: " + "\n" +  text + "\n"  + "Hashtags: " + "\n" + hashtext + "\n"

                

                i = i+1
            encrypt()
            return iTweet

