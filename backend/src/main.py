from flask_cors import CORS
from flask import Flask, jsonify, request
from sqlalchemy import desc

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema
from .entities.hateSpeech import HateSpeech, HateSpeechSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/exams')
def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201













@app.route('/hatespeech')
def get_hatespeech():
    result = {'numberOfHateSpeechTweetsInLast2Minutes' : '23'}
    return result
    # # fetching from the database
    # session = Session()
    # hateSpeech_objects = session.query(HateSpeech).order_by(desc(HateSpeech.created_at)).first()

    # # transforming into JSON-serializable objects
    # schema = HateSpeechSchema(many=False)
    # hatespeech = schema.dump(hateSpeech_objects)

    # # serializing as JSON
    # session.close()
    # return jsonify(hatespeech)


# @app.route('/hatespeech', methods=['POST'])
# def add_hatespeech():
    
#     # try:
#         # data = request.get_json()
#     # numberOfHateSpeechTweetsIn2Minutes = data['numberOfHateSpeechTweetsIn2Minutes']
#     #     hatespeech = HateSpeech(numberOfHateSpeechTweetsIn2Minutes, "Created by request")
      
#     #     # persist hatespeech
#     #     session = Session()
#     #     session.add(hatespeech)
#     #     session.commit()

#     #     # return created exam
#     #     # new_hatespeech = HateSpeechSchema().dump(hatespeech).data
#     #     session.close()
#     # except Exception as e:
#     #     print(e)
#     #     return str(e), 500
#     # else:
#         return "hello", 201