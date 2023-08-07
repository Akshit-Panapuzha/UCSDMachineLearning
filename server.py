from flask import Flask, request, jsonify

app = Flask(__name__)

def run_ml_process(input_data):
    return 1

@app.route('/api', methods=['POST'])
def process_input():

    input_data = request.get_json()
    result = run_ml_process(input_data)  # Placeholder function, replace it with your ML code.
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)