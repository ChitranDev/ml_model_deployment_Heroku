
import pickle
import numpy as np
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
model = pickle.load(open('student_pickle_model','rb'))





@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods = ['POST'])
def predict():
    
        
    english_p = request.form.get('english_p')
    hindi_p = request.form.get('hindi_p')
    math_p = request.form.get('maths_p')
    science_p = request.form.get('science_p')
    sst_p = request.form.get('sst_p')
    print(english_p)

    try:
        subjects = [int(english_p),int(hindi_p),int(math_p),int(science_p),int(sst_p)]
        final_features = [np.array(subjects)]
        prediction = model.predict(final_features)
        final_result = np.round(prediction, 2)
        print(final_result)

        if int(final_result) > 100:
            full = [99.99]
            
            final_result = full

    except Exception as e:
        print(e)
        print('error occured')

    return render_template('result.html', prediction_text = final_result[0])
    









if __name__ == "__main__":
    app.run(debug=True)
