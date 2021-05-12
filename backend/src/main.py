from flask_cors import CORS
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from sqlalchemy import desc, func
from .baseEntity import Session, engine, Base
from .hateSpeech import HateSpeechModel, HateSpeechSchema
from .tweets import TweetModel, TweetSchema
from .twitterStream import streamTweets
from threading import Thread
from datetime import datetime, timedelta
from collections import OrderedDict


# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

@app.route('/tweets')
def get_tweets():
    session = Session()
    TweetModel_objects = session.query(TweetModel).order_by(desc(TweetModel.created_at)).limit(15).all()

    # transforming into JSON-serializable objects
    schema = TweetSchema(many=True)
    tweets = schema.dump(TweetModel_objects)

    # serializing as JSON
    session.close()
    return jsonify(tweets)


@app.route("/startStream")
def index():
    thread = Thread(target=streamTweets, args=())
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})

if __name__=='__main__':
    app.run(port='5000')

@app.route('/tweets/perinterval')
def get_tweets_per_minute():
    session = Session()

    searchDate = datetime.now() + timedelta(days=-2)

    #get count of tweets for each minute in a given time frame
    rows = session \
            .query(func.to_char(TweetModel.created_at, 'MI'), func.count(TweetModel.id)) \
            .where(TweetModel.created_at > searchDate) \
            .group_by(func.to_char(TweetModel.created_at, 'MI')) \
            .order_by(func.to_char(TweetModel.created_at, 'MI')) \
            .all()

    session.close()

    #read rows into array list to turn into json
    object_list = []
    for row in rows:
        d = OrderedDict()
        d['minute'] = row[0]
        d['count'] = row[1]
        object_list.append(d)

    return jsonify(object_list)
