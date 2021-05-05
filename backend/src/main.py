from flask_cors import CORS
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Flask, jsonify, request
from sqlalchemy import desc

from .baseEntity import Session, engine, Base
#from entities.exam import Exam, ExamSchema
from .hateSpeech import HateSpeechModel, HateSpeechSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

@app.route('/hatespeech')
def get_hatespeech():
    # result = {'numberOfHateSpeechTweetsInLast2Minutes' : '23'}
    # return result
    # fetching from the database
    session = Session()
    hateSpeech_objects = session.query(HateSpeechModel).order_by(desc(HateSpeechModel.created_at)).first()

    # transforming into JSON-serializable objects
    schema = HateSpeechSchema(many=False)
    hatespeech = schema.dump(hateSpeech_objects)

    # serializing as JSON
    session.close()
    return jsonify(hatespeech)


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


if __name__ == '__main__':
     app.run(port='5002')