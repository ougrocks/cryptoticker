from django.test import TestCase

# Create your tests here.
import requests, json
def get(self, *args, **kwargs):
    url = 'https://bittrex.com/Api/v2.0/pub/currencies/GetBTCPrice'

    headers = {
        'host': "bittrex.com",
        'connection': "keep-alive",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'referer': "https://bittrex.com/home/markets",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "__cfduid=dc8969bd3cf7ce991eb6db16dbb7864a61513575280; __RequestVerificationToken=rnZgQUn6IS4Qpi32YPKUBPaNmVEC57uOsd4rhXb7rAnaRkiiUvNWwxiq8N5VpjILIhG5SJlpjWszvoGRUM1TT-lLXHU1; cf_clearance=0413c3284b2afd4d1ba8b2d354ffd05fa9692dc3-1514964151-10800",
        'if-modified-since': "Wed, 03 Jan 2018 07:54:00 GMT",
        'cache-control': "no-cache",
        'postman-token': "d2991c5e-c3c4-b686-ade1-6906aa5e9bb8"
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    time_price = json.loads(response.text)['result']['time']['updated']
    print(time_price)
    return Response({'btc': json.loads(response.text)['result']['bpi']['USD']['rate_float']})