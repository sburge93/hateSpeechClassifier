import pickle

classifier = pickle.load(open('./backend/random_forest_model.sav', 'rb'))
result = classifier.predict(['blah'])
print(result)
print('the result is')
print(result[0])