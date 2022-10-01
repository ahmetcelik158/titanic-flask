from model import Predictor

my_dict = {"Pclass": 2,
            "Title": "Mrs",
            "Name": "Hello",
            "Surname": "World",
            "Sex": "female",
            "Age": 32,
            "SibSp": 2,
            "Parch": 0,
            "Fare": 220,
            "Embarked": "C"}

if __name__ == "__main__":
    p = Predictor()
    p.load_dict(my_dict)
    probs, survival = p.predict()
    print(probs, survival)
    