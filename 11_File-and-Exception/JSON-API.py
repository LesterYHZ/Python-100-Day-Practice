"""
Many website API use JSON to store the data
In this case, tianapi.com provides a news API
replace APIKey with a real Key which cost 0.0001 RMB per day
"""
import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.load(resp.txt)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == "__main__":
    main()