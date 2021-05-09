from marshmallow import Schema, fields
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import Column, String, DateTime
from flask import Flask
from .baseEntity import Entity, Base
from datetime import datetime
# app = Flask(__name__)
# ma = Marshmallow(app)




class TweetModel(Entity, Base):
    __tablename__ = 'tweets'

    tweet = Column(String)
    tweetDate = Column(DateTime)

    def __init__(self, tweet, tweetDate, created_by):
        Entity.__init__(self, created_by)
        self.tweet = tweet
        self.tweetDate = tweetDate

class TweetSchema(ModelSchema):
    class Meta:
        model = TweetModel
