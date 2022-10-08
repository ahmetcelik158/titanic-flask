# Would you survive Titanic?

* Created a Web UI using Flask to predict the survival chance of a person from Titanic.
* The machine learning model that predicts survival is taken from my own Kaggle project which has an accuracy of 79%.
* In this project, application takes the necessary information from the client and returns the survival chance.
* ML Model Reference: https://www.kaggle.com/code/ahmetcelik158/titanic

## Packages:

**Python Version:** 3.9.7

**Installing Requirements:** ```pip install -r requirements.txt```

## Input Data Format
* Title: [string] "Miss", "Mr", "Mrs", "Master" or "Other"
* First Name: [string]
* Last Name: [string]
* Sex: [string] "female" or "male"
* Age: [int] between 0 and 120
* Number of siblings & spouses: [int] between 0 and 8
* Number of parents & children: [int] between 0 and 8
* Port of Embarkation: [string] "C", "Q" or "S"
* Ticket Class: [int] 1, 2 or 3
