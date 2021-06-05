import requests
import os
import json
import pickle
from .tweets import TweetModel, TweetSchema
from .baseEntity import Session, engine, Base
from datetime import datetime
from dateutil import parser

document_path = os.getcwd()+'/backend/src/random_forest_model.sav'
document = open(document_path, 'rb')
classifier = pickle.load(document)


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(headers, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [
         {"value": "brexit"},
        {"value": "corona virus"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream?tweet.fields=text,created_at", headers=headers, stream=True,
    )
   
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )

    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            #print(json.dumps(json_response, indent=4, sort_keys=True))

            tweet = json_response['data']['text']
            print('tweet text is ' + tweet)

            createdAt = parser.parse(json_response['data']['created_at'])
            print(createdAt)

            result = classifier.predict([tweet])
            print('the result is')
            print(result)

            if result[0] == 0:
                SaveTweet(tweet, createdAt)


def SaveTweet(tweet, tweetDate):
    tweets = TweetModel(tweet, tweetDate, "Created by request")
    print(tweets.tweet)
    session = Session()
    session.add(tweets)
    session.commit()
    session.close()

def streamTweets():
    print('in streamTweets')
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJf8PAEAAAAAzQONMQ38F7cu82gxvWPJA%2BBot18%3DdxtRyyaMczSOesv0PLWG3gAXz99gs6bVL4oLUB5cJB3LpEHB4o'
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete_all_rules(headers, bearer_token, rules)
    set_rules(headers, bearer_token)
    get_stream(headers, bearer_token)



if __name__ == "__main__":
    streamTweets()