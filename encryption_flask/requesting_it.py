import requests
import json


def encrypt_with_api():
    url = "http://127.0.0.1:5000/api"

    headers = {
        "Content-Type" : "application/json"
    }

    json_data = {
        "state": "decrypt",
        "message": "gAAAAABn7pg8feFQLyS8S5HXhVP2eW-qTC72MSnQvFSSptLl5eS9h_TGcbyT_pK5HSBR0Vl-8ppCKfLjHeyXdJD16JTC2_YlLA=="
    }

    response = requests.post(url=url, headers=headers, json=json_data)
    r = json.loads(response.text)

    print(r)
    print(r["message"])

if __name__ == "__main__" :
    encrypt_with_api()