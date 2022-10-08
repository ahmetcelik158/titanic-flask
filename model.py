import pickle
import pandas as pd
from numpy import log

class Predictor:
    def __init__(self) -> None:
        file_name = "model_file.p"
        with open(file_name, 'rb') as pickled:
            loaded_pickle = pickle.load(pickled)
        self.model = loaded_pickle["model"]
        self.scaler = loaded_pickle["scaler"]

    def load_dict(self, data_dict):
        # Family type:
        data_dict["FamSize"] = data_dict["SibSp"] + data_dict["Parch"]
        data_dict["FamType_Alone"] = 0
        data_dict["FamType_Small_Family"] = 0
        if data_dict["FamSize"] == 0:
            data_dict["FamType_Alone"] = 1
        elif data_dict["FamSize"] < 4:
            data_dict["FamType_Small_Family"] = 1
            
        # Title:
        data_dict["TitleProcessed_ Master"] = 0
        data_dict["TitleProcessed_ Miss"] = 0
        data_dict["TitleProcessed_ Mr"] = 0
        data_dict["TitleProcessed_ Mrs"] = 0
        if data_dict["Title"] == "Master":
            data_dict["TitleProcessed_ Master"] = 1
        elif data_dict["Title"] == "Miss":
            data_dict["TitleProcessed_ Miss"] = 1
        elif data_dict["Title"] == "Mr":
            data_dict["TitleProcessed_ Mr"] = 1
        elif data_dict["Title"] == "Mrs":
            data_dict["TitleProcessed_ Mrs"] = 1

        # Fare:
        data_dict["Fare"] = 85 # 1st class
        if data_dict["Pclass"] == 2: # 2nd class
            data_dict["Fare"] = 42
        elif data_dict["Pclass"] == 3: # 3rd class
            data_dict["Fare"] = 9
        data_dict["FareLog"] = log(data_dict["Fare"]+14.4542)

        # Sex:
        data_dict["Sex_male"] = 0
        if data_dict["Sex"] == "male":
            data_dict["Sex_male"] = 1

        # Embarked:
        data_dict["Embarked_C"] = 0
        data_dict["Embarked_S"] = 0
        if data_dict["Embarked"] == "C":
            data_dict["Embarked_C"] = 1
        elif data_dict["Embarked"] == "S":
            data_dict["Embarked_S"] = 1

        cols = ["Pclass", "Age", "FareLog", "TitleProcessed_ Master",
                "TitleProcessed_ Miss", "TitleProcessed_ Mr",
                "TitleProcessed_ Mrs", "Sex_male", "FamType_Alone",
                "FamType_Small_Family", "Embarked_C", "Embarked_S"]
        df = pd.DataFrame(data_dict, index=[0])
        self.df = df[cols]
        return

    def predict(self):
        df_scaled = self.scaler.transform(self.df)
        survival = self.model.predict(df_scaled)
        probs = self.model.predict_proba(df_scaled)
        return int(survival[0]), float(probs[0][1])

