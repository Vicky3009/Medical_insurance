
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import Medical_Insurance
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("sample.html")

@app.route('/charges',methods=['POST','GET'])

def predicion_premium():

    if request.method =='GET':

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

    # data = request.form
    # age = data['age']
    # sex = data["sex"]
    # bmi = data['bmi']
    # children = data['children']
    # smoker = data['smoker']
    # region = data['region']
    
        

        OBJ = Medical_Insurance(age, sex, bmi, children, smoker, region)
        Insurance_charge = OBJ.prediction()
        #return jsonify({'Result' : Insurance_charge })
        return render_template('sample.html',prediction = Insurance_charge)
    else:
        

        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        OBJ = Medical_Insurance(age, sex, bmi, children, smoker, region)
        Insurance_charge = OBJ.prediction()
        #return jsonify({'Result' : Insurance_charge })
        return render_template('sample.html',prediction = Insurance_charge)

if __name__ == '__main__':
    
    app.run(debug=True)
