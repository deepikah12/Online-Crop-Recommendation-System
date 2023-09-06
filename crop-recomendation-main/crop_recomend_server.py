from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('crop_recomend.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form.to_dict()
    input = []
    for key, value in form_data.items():
        input.append(value)
    
    input=[input]
    output=model.predict(input)
    response="<center> <h1> The recomended crop is : "+output[0]+"</h1></center>"
    return response
    

if __name__ == '__main__':
    # Run the Flask application
    app.run()