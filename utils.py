import requests


def get_data_from_api():
    url = 'https://tradestie.com/api/v1/apps/reddit'
    response = requests.get(url)
    return response.json()
