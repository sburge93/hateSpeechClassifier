import pickle

classifier = pickle.load(open('./backend/src/randomForest_model.sav', 'rb'))
result = classifier.predict("some hatespeech")
print(result)