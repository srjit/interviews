import joblib


classifier = joblib.load('survive_prediction.pkl')
print("Enter the following details to make the predictions:- n")


pclass = int(intput("Enter The Pclass:- "))
Age = int(intput("Enter The Age:- "))
SibSP = int(intput("Enter The SibSp:- "))
Parch = int(intput("Enter The Parch:- "))
Sex = int(intput("Enter The Sex:- "))

passenger_prediction = classifier.predict([[pclass,Age,SibSP,Parch,Sex]])

if passenger_prediction == 0:
print("Not Survived.")
else ;

print("Survived")