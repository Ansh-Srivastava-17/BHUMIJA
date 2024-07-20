from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('IndiaWeatherModel_pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    prcp = float(request.form['prcp'])
    tmax = float(request.form['tmax'])
    tmin = float(request.form['tmin'])
    city_name = int(request.form['city_name'])  # Assuming city name is represented as an integer
    
    # Make prediction
    input_data = pd.DataFrame({'prcp': [prcp], 'tmax': [tmax], 'tmin': [tmin], 'city-Name': [city_name]})
    prediction = model.predict(input_data)
    
    # Pass prediction to results page
    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
