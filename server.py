from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

def run_ml_process(input_data):
    # Load the trained model from the .pkl file
    model_filename = 'stock_price_prediction_model.pkl'
    loaded_model = joblib.load(model_filename)

    #print("Loaded Model: ", loaded_model)

    # Define test inputs (replace with your actual test inputs)
    #test_inputs = [
    #    {"Low": 20.899999618530273, "Open": 20.899999618530273, "High": 21.75, "Close": 21.5}
        # Add more test inputs as needed
    #]

    # Convert test inputs into a DataFrame
    #test_df = pd.DataFrame(input_data)

    input_df = pd.DataFrame.from_dict(input_data, orient='index').transpose()

    # Make predictions using the loaded model
    predicted_values = loaded_model.predict(input_df)

    predicted_values_list = predicted_values.tolist()

    # Display the predictions for each test input
    return predicted_values_list

@app.route('/api', methods=['POST'])
def process_input():

    input_data = request.get_json()
    result = run_ml_process(input_data)  # Placeholder function, replace it with your ML code.
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)