# Would you survive Titanic?

* Created an API using Flask to predict the survival chance of a person from Titanic.
* The machine learning model that predicts survival is taken from my own Kaggle project which has an accuracy of 79%.
* In this project, API endpoint takes the necessary information from the client and returns the survival chance.
* ML Model Reference: https://www.kaggle.com/code/ahmetcelik158/titanic

## Packages:

**Python Version:** 3.9.7

**Installing Requirements:** ```pip install -r requirements.txt```

## Data Format For API Endpoint
* Pclass: [int] 1, 2 or 3
* Title: [string] "Miss", "Mr", "Mrs", "Master" or "Other"
* Name: [string]
* Surname: [string]
* Sex: [string] "female" or "male"
* Age: [int] between 0 and 120
* SibSp: [int] between 0 and 8
* Parch: [int] between 0 and 8
* Fare: [int] between 0 and 520
* Embarked: [string] "C", "Q" or "S"

## Example Usage of API Endpoint:
```python
import requests, json

data = {"Pclass": 2,
        "Title": "Mrs",
        "Name": "Hello",
        "Surname": "World",
        "Sex": "female",
        "Age": 24,
        "SibSp": 2,
        "Parch": 0,
        "Fare": 220,
        "Embarked": "C"}
data_json = json.dumps(data)

URL = 'http://127.0.0.1:8080/'
r = requests.post(URL, json=data_json) 
print(r)
print(r.json())
```
```
<Response [200]>
{'survival': 1, 'probability': 0.83807222257506}
```