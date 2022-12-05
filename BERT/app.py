from sklearn.preprocessing import LabelEncoder
from simpletransformers.classification import ClassificationModel
import pickle

import os
import re
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


target = ['anger','fear','joy','love','sadness','surprise']
le=LabelEncoder()
coded=le.fit_transform(target)

label=''
sentence=''

@app.route("/")
def home():
    
    return render_template('index.html')

@app.route("/emotion",methods = ['POST', 'GET'])
def emotion():

    label=''
    sentence=''

    if request.method == "POST":
        bert=pickle.load(open('bert.pkl','rb'))
        sentence=request.form['sentence']
        prediction=bert.predict([sentence])
        label=le.inverse_transform(prediction[0])[0]
        print(sentence)
        print(request.form["sentence"])
        return render_template('sad.html',output=label)
        
    # else:
    #     prediction=""
    #     print('i hate my life')
    return render_template('emotion.html')


if __name__ == '__main__':
    app.run()