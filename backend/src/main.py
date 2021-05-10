from flask_cors import CORS
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from sqlalchemy import desc
from .baseEntity import Session, engine, Base
from .hateSpeech import HateSpeechModel, HateSpeechSchema
from .tweets import TweetModel, TweetSchema
from .twitterStream import streamTweets
import threading


# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

@app.route('/tweets')
def get_tweets():
    # result = {'numberOfHateSpeechTweetsInLast2Minutes' : '23'}
    # return result
    # fetching from the database
    session = Session()
    TweetModel_objects = session.query(TweetModel).order_by(desc(TweetModel.created_at)).first()

    # transforming into JSON-serializable objects
    schema = TweetSchema(many=False)
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

def RunApi():
    app.run(port='5002')
    streamTweets()
    # thread = threading.Thread(target=streamTweets(), args=())
    # thread.daemon = True
    # # Daemonize thread
    # thread.start()

if __name__=='__main__':
    RunApi()