import numpy as np
import pandas as pd
import pickle
import json



class Medical_Insurance():
    def __init__(self, age,  sex ,  bmi ,  children ,  smoker ,  region):
         self.age = age
         self.sex = sex 
         self.bmi = bmi
         self.children = children
         self.smoker = smoker
         self.region = 'region_' + region


    def load_model(self):
        # Loading pickle file
        with open(r"C:\Users\HP\Desktop\New folder (2)\models\Linear_regression.pkl",'rb')as f:
            self.lin_reg_model = pickle.load(f)
        

        # Loading json file
        with open(r"C:\Users\HP\Desktop\New folder (2)\models\project_data.json",'r')as f:
            self.json_data = json.load(f)

    def prediction(self):
        self.load_model() # Calling load_model method to get model and json_data


        region_index = self.json_data['columns'].index(self.region)

        array = np.zeros(len(self.json_data['columns']))
        array[0] = self.age
        array[1] = self.json_data['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data['smoker'][self.smoker]
        array[region_index] = 1
        

        predicted_charge = self.lin_reg_model.predict([array])[0]
        print('Test Array --->>> ',array)
        print('Predicted Charges',predicted_charge)
        return np.around(predicted_charge, 2)


if __name__ == '__main__':
    age = 67
    sex = "male"
    bmi = 27.9
    children = 3
    smoker = "yes"
    region = "southeast"

    charge = Medical_Insurance(age, sex, bmi, children, smoker, region)
    Insurance_charge = charge.prediction()
    print(f"Predicted Charges for Medical Insurance is {Insurance_charge}/-- Rs only")

