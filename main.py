import json
from flask import Flask,Flask,render_template,request,jsonify, url_for
import numpy as np
import pandas as pd
import pickle

project_app = Flask(__name__)

@project_app.route('/')
def index():
    return render_template('project_front.html')

@project_app.route('/user_data',methods = ['POST'])
def getting_data():
    data = request.form
    user_name = data['n1']
    user_email = data['e1']
    user_gender = data['G1']
    user_state = data['s1']
    user_age = data['a1']
    user_bmi = float(data['b1'])
    user_childern = data['o1']
    user_smoke = data['y1']
    

    data = np.array([user_age,user_gender,user_bmi,user_childern,user_smoke],ndmin=2)
    # age	sex	bmi	children	smoker	region	
    with open('final_modle.pkl','rb') as file:
        model_final = pickle.load(file)

    result_final = np.around(model_final.predict(data),3)    
    
    return render_template('haha.html',name=user_name,em=user_email,st=user_state,gn=user_gender,ag=user_age,bm=user_bmi,ch=user_childern,res= result_final[0])



if __name__ == '__main__':
    project_app.run(debug = True)    