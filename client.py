import requests

def send_data_to_server(data):
    header = {"Content-Type": "application/json"}
    url = 'http://34.210.58.76:5000/api'  # Replace YOUR_EC2_PUBLIC_IP with your EC2 instance's public IP address.
    response = requests.post(url, json=data, headers=header)
    
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == '__main__':
    # Replace this example data with your actual data that you want to send to the server.
    
    example_data = {"input_1": 42, "input_2": 3.14}
    result_from_server = send_data_to_server(example_data)
    print("Result from server:", result_from_server)
