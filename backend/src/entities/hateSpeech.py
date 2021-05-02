from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class HateSpeech(Entity, Base):
    __tablename__ = 'hatespeech'

    numberOfHateSpeechTweetsInLast2Minutes = Column(String)

    def __init__(self, numberOfHateSpeechTweetsInLast2Minutes, created_by):
        Entity.__init__(self, created_by)
        self.numberOfHateSpeechTweetsIn2Minutes = numberOfHateSpeechTweetsInLast2Minutes

class HateSpeechSchema(Schema):
    id = fields.Number()
    numberOfHateSpeechTweetsInLast2Minutes = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
   