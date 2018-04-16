import sys
from textblob import TextBlob
import matplotlib.pyplot as plt
from tweepy import OAuthHandler,API,Cursor

ck = 'TSwFRDLymWY6x8nN3nRnIaN4f'
cs = 'SY7Xg4zLWBuvfm0DIka0o9t8AOBGfgwXh3c8SJ4ggFsEfXbXsW'
at = '2469634638-a0RETZDdnHjkKmIGNJTt3HCVGLTgb3LCIIxjoOf'
ats = 'SBH91pzExI0IHqEdSYmmN7Cde5vqTo19HFM46SPKAqqjp'

auth = OAuthHandler(ck,cs)
auth.set_access_token(at,ats)
api = API(auth)


term = "Pakistan"
noterm = 1000
tweets = Cursor(api.search, q=term)
tweets = tweets.items(noterm)
positive = 0
negative = 0
neutral = 0
for t in tweets:
    value = TextBlob(t.text)
    if(value.sentiment.polarity==0):
        neutral+=1
    elif(value.sentiment.polarity>0):
        positive+=1
    elif (value.sentiment.polarity < 0):
        negative += 1


neutral = (neutral/noterm)*100
positive = (positive/noterm)*100
negative = (negative/noterm)*100

labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
explode = (0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Popularity graph of search term: "+term)
plt.show()
