from flask import Flask,request
import pickle
import flasgger
from flasgger import Swagger

#create the object
app=Flask(__name__)
Swagger(app)

#import the pickle file
pickle_in=open('Banknote.pkl','rb')
classifier=pickle.load(pickle_in)

#index page
@app.route('/')
def index():
    return 'BANK NOTE AUTHENTICATION'

#predict page
@app.route('/predict',methods=['GET']) 
def result():
    
    """ Bank Note Authentication
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The Output Values
    """
        
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if prediction==0:
        res='It is a Fake note'
    else:
        res='It is a orginal note'
    return res

#to run
if __name__=='__main__':
    app.run(debug=False)

