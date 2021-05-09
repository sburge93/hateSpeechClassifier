import pickle
from .tweets import TweetModel, TweetSchema
from .baseEntity import Session, engine, Base
from datetime import datetime

Base.metadata.create_all(engine)

def SaveTweet(tweet, tweetDate):
    tweets = TweetModel(tweet, tweetDate, "Created by request")
    print(tweets.tweet)
    session = Session()
    session.add(tweets)
    session.commit()
    session.close()


classifier = pickle.load(open('./backend/random_forest_model.sav', 'rb'))
result = classifier.predict(['momma said no pussy cats inside my doghouse'])
print('the result is')
print(result)

tweet = 'some tweet text' 
tweetDate = datetime(2021, 5, 17)
SaveTweet(tweet, tweetDate)
