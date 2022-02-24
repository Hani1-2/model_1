from flask import flash, Flask, render_template, request
import pickle
import urllib.request
import os
from werkzeug.utils import secure_filename
import numpy as np
model = pickle.load(open('model_pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/prime')
def prime():
    return render_template('prime.html')

@app.route('/predict', methods=['POST'])
def predict():
    arr = []
    if request.method == 'POST':
        data1 = request.form['a']
        if data1 != None:
            arr.append(data1)
        else:
            data1 = 0
            arr.append(data1)
        data2 = request.form['b']
        if data2 != None:
            arr.append(data2)
        else:
            data2 = 0
            arr.append(data2)
        data3 = request.form['c']
        if data3 != None:
            arr.append(data3)
        else:
            data3 = 0
            arr.append(data3)
        data4 = request.form['d']
        if data4 != None:
            arr.append(data4)
        else:
            data4 = 0
            arr.append(data4)
        data5 = request.form['e']
        if data5 != None:
            arr.append(data5)
        else:
            data5 = 0
            arr.append(data5)
        data6 = request.form['f']
        if data6 != None:
            arr.append(data6)
        else:
            data6 = 0
            arr.append(data6)
        data7 = request.form['g']
        if data7 != None:
            arr.append(data7)
        else:
            data7 = 0
            arr.append(data7)
        data8 = request.form['h']
        if data8 != None:
            arr.append(data8)
        else:
            data8 = 0
            arr.append(data8)
        data9 = request.form['i']
        if data9 != None:
            arr.append(data9)
        else:
            data1 = 0
            arr.append(data9)
        data10 = request.form['j']
        if data10 != None:
            arr.append(data10)
        else:
            data10 = 0
            arr.append(data10)
        data11 = request.form['k']
        if data11 != None:
            arr.append(data11)
        else:
            data11 = 0
            arr.append(data11)
        data12 = request.form['l']
        if data12 != None:
            arr.append(data12)
        else:
            data12 = 0
            arr.append(data12)
        data13 = request.form['m']
        if data13 != None:
            arr.append(data13)
        else:
            data13 = 0
            arr.append(data13)
        data14 = request.form['n']
        if data14 != None:
            arr.append(data14)
        else:
            data14 = 0
            arr.append(data14)
        data15 = request.form['o']
        if data15 != None:
            arr.append(data15)
        else:
            data15 = 0
            arr.append(data15)
        data16 = request.form['p']
        if data16 != None:
            arr.append(data16)
        else:
            data16 = 0
            arr.append(data16)
        data17 = request.form['q']
        if data17 != None:
            arr.append(data17)
        else:
            data17 = 0
            arr.append(data17)
        data18 = request.form['r']
        if data18 != None:
            arr.append(data18)
        else:
            data18 = 0
            arr.append(data18)
        data19 = request.form['s']
        if data19 != None:
            arr.append(data19)
        else:
            data19 = 0
            arr.append(data19)
        data20 = request.form['t']
        if data20 != None:
            arr.append(data20)
        else:
            data20 = 0
            arr.append(data20)
        data21 = request.form['u']
        if data21 != None:
            arr.append(data21)
        else:
            data21 = 0
            arr.append(data21)
        data22 = request.form['v']
        if data22 != None:
            arr.append(data22)
        else:
            data22 = 0
            arr.append(data22)
        data23 = request.form['w']
        if data23 != None:
            arr.append(data23)
        else:
            data23 = 0
            arr.append(data23)
        data24 = request.form['x']
        if data24 != None:
            arr.append(data24)
        else:
            data24 = 0
            arr.append(data24)
        arr1 = np.array([arr])
        pred = model.predict(arr1).reshape(1, -1)
        print(pred)
        return render_template("prime.html", data=pred)













if __name__ == "__main__":
    app.run(debug=True)