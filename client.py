import requests

def send_data_to_server(data):
    header = {"Content-Type": "application/json"}
    url = 'http://35.167.2.31:5000/api'
    response = requests.post(url, json=data, headers=header)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == '__main__':
    # Replace this example data with your actual data that you want to send to the server.
    print("example_data = \n{'Low': 20.899999618530273,\n'Open': 20.899999618530273,\n'Adjusted Close': 24.5,\n'High': 21.75,\n'Close': 21.5,\n#}")
    low = input("low: ")
    open = input("open: ")
    adjclose = input("adjusted close: ")
    high = input("high: ")
    close = input("close: ")

    example_data = {
        "Low": low,
        "Open": open,
        "Adjusted Close": adjclose,
        "High": high,
        "Close": close,
    }

    #example_data = {
    #    "Low": 20.899999618530273,
    #    "Open": 20.899999618530273,
    #    "Adjusted Close": 24.5,
    #    "High": 21.75,
    #    "Close": 21.5,
    #}
    result_from_server = send_data_to_server(example_data)
    print("Days From the Start to Get to the Listed Values:", result_from_server)
