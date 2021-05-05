from marshmallow import Schema, fields
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import Column, String
from flask import Flask
from .baseEntity import Entity, Base

# app = Flask(__name__)
# ma = Marshmallow(app)




class HateSpeechModel(Entity, Base):
    __tablename__ = 'hatespeechnew'

    numberOfHateSpeechTweetsInLast2Minutes = Column(String)

    def __init__(self, numberOfHateSpeechTweetsInLast2Minutes, created_by):
        Entity.__init__(self, created_by)
        self.numberOfHateSpeechTweetsInLast2Minutes = numberOfHateSpeechTweetsInLast2Minutes

class HateSpeechSchema(ModelSchema):
    class Meta:
        model = HateSpeechModel
