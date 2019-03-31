import tweepy as tp  # tweepy library, allows interface with twitter
import time as Thread
import pymysql as sql
import random as rand
import threading

# connection = sql.connect(host='localhost',
#                          user='user',
#                          password='passwd',
#                          db='db',
#                          charset='utf8mb4',
#                          cursorclass=sql.cursors.DictCursor)

# noinspection SpellCheckingInspection
consumerKey = "gog240fEc8iSZAlmP5OMtiz7o"
# noinspection SpellCheckingInspection
consumerSecret = "uPClNj603GQ2BWhrtTprheHWGCNo9AzR6j9BmS8I06keaqU3IZ"
# noinspection SpellCheckingInspection
accessKey = "1112030738776539139-8UYcSp4vkX18f0bo8WR6qm9khl5Zzl"
# noinspection SpellCheckingInspection
accessSecret = "1QaIl3mKS7mNrb8GGyx0WDQOMw97XufmO1RLkow8U4itm"

auth = tp.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tp.API(auth)
user = api.me()
# TODO: Export user information as sql

for follower in tp.Cursor(api.followers).items():  # follows all accounts following the bot, and gets data from them
    follower.follow()

print("Followed everyone following Sweatmeet.")


def writeTweet(message):  # Writes a tweet, provided a message
    api.update_status(message)

    return True


messages = ["Follow this bot to be subscribed to receive requests for pickup #football games in your area #hawkhack "
            "#hackathon #spambot #python",
            "To be informed of local #football games in your area, follow this bot. #hawkhack #hackathon #spambot "
            "#python",
            "Subscibe to this bot to be kept informed of pickup #football games in your area #hawkhack #hackathon "
            "#spambot #python"]  # TODO: Write list of possible messages
'''
while True:  # A really sloppy, really disgusting workaround that sends a new message every hour.
    writeTweet(messages[rand.randrange(0, 3)])  # TODO: Write random message here from messages list
    Thread.sleep(3600)  # Exactly 1 hour
    '''


def send_message():
    messageToSend = [
        "Follow this bot to be subscribed to receive requests for pickup #football games in your area #hawkhack "
        "#hackathon #spambot #python",
        "To be informed of local #football games in your area, follow this bot. #hawkhack #hackathon #spambot "
        "#python",
        "Subscibe to this bot to be kept informed of pickup #football games in your area #hawkhack #hackathon "
        "#spambot #python"]
    while True:
        try:
            sent = messageToSend[rand.randrange(0, 2)]
            writeTweet(sent)
            print(sent)
        except tp.error.TweepError:
            print(sent + " is a duplicate message. Reassigning.")
            sent = messageToSend[rand.randrange(0, 2)]
        finally:
            Thread.sleep(3600)  # Exactly 1 hour


def checkingFollowers(tweetpy):
    while True:
        for follower in tweetpy.Cursor(api.followers).items():
            follower.follow()
            print("Followed back " + follower.username)
            print("Follower Information:")
            print(follower.username, follower.location, follower.name, follower.id)
        Thread.sleep(3600)  # Exactly 1 hour


sendMessageThread = threading.Thread(target=send_message())
sendMessageThread.start()
followerChecker = threading.Thread(target=checkingFollowers(tp))
followerChecker.start()
