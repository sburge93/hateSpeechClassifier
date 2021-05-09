import pickle

classifier = pickle.load(open('./backend/random_forest_model.sav', 'rb'))
result = classifier.predict(['momma said no pussy cats inside my doghouse'])
print('the result is')
print(result)