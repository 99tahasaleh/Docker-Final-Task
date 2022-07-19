from flask import Flask, render_template
import requests
import redis

app = Flask(__name__)

redis = redis.Redis(host='redis', port=6379)

#get the current price of Bitcoin
# import data from the json format website, extract the price column and ass to database
def get_current_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        data_responce = requests.get(url)
        extracted_price = data_responce.json()['price']
        # add to redis data base
        redis.set('price_of_Bitcoin', extracted_price)
    except Exception as exp:
        print(exp)
    return extracted_price

def get_avg_price():
    url = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"
    try:
        data_responce = requests.get(url)
        prices= data_responce.json()['Data']['Data']
        sum = 0
        average = 0.0

        #iterate through the prices array to sum the prices
        for price in prices:
            sum += price['close']

        average = sum / 10
        redis.set('avg10', average)
    except Exception as exp:
        print(exp)
    return average

@app.route('/')
def bitcoinApp():
    return render_template('bitcoinapp.html',message1=get_current_price(),message2=get_avg_price())



if __name__ == "__main__":
    app.run(host = "0.0.0.0")