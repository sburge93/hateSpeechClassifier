from flask_cors import CORS
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from sqlalchemy import desc
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

@app.route('/hatespeech', methods=['POST'])
def add_hatespeech():
    
    try:
        data = request.get_json()
        print(data)
        numberOfHateSpeechTweetsIn2Minutes = data.get('numberOfHateSpeechTweetsInLast2Minutes', '')
        print(numberOfHateSpeechTweetsIn2Minutes)
        hatespeech = HateSpeechModel(numberOfHateSpeechTweetsIn2Minutes, "Created by request")
        print(hatespeech.numberOfHateSpeechTweetsInLast2Minutes)
        # persist hatespeech
        session = Session()
        session.add(hatespeech)
        session.commit()

        # return created exam
        # new_hatespeech = HateSpeechSchema().dump(hatespeech).data
        session.close()
    except Exception as e:
        print(e)
        return str(e), 500
    else:
        return jsonify("hello"), 201

@app.route("/startStream")
def index():
    thread = Thread(target=streamTweets, args=())
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})

if __name__=='__main__':
    app.run(port='5002')

@app.route('/tweets/perinterval')
def get_tweets_per_minute():
    session = Session()

    searchDate = datetime.now() + timedelta(days=-2)

    #get count of tweets for each minute in a given time frame
    rows = session \
            .query(func.strftime("%M",TweetModel.created_at), func.count(TweetModel.id)) \
            .where(TweetModel.created_at > searchDate) \
            .group_by(func.strftime("%M",TweetModel.created_at)) \
            .order_by(func.strftime("%M",TweetModel.created_at)) \
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
