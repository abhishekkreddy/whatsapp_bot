from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
@app.route('/bot',methods=['post'])
def bot():
    incoming_msg = request.values.get('Body','').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    if "hi" in incoming_msg or "hey" in incoming_msg or "menu" in incoming_msg:
        result = f'Hello humans🙋‍♂‍🙋‍♀‍,\nIm a bot who is here to to keep you updated about real time *CRYPTO PRICES* \n👉To get *BITCOIN* Price enter *BTC* \n👉for *LITECOIN* Price eenter *LTC* \n👉for *ETHERIUM* Price enter *ETH* \n👉for *DOGECOIN* Price enter *DOGE* \n👉for *CHAINLINK* Price enter *LINK* \n👉for *TEZOS* Price enter *XTZ* \n👉for *CARDANO* Price enter *ADA*  '
        msg.body(result)
        responded = True
    if "BTC" in incoming_msg or "btc" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/BTC/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex='OPEN :'+str(y["open"]) +'\n' + 'Close :' +str(y["close"])
            tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
          tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True

    if "LTC" in incoming_msg or "ltc" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/LTC/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
           # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True
    if "ETH" in incoming_msg or "eth" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/ETH/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
            # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True

    if "DOGE" in incoming_msg or "doge" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/DOGE/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
            # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True

    if "ADA" in incoming_msg or "ada" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/ADA/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
            # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True

    if "LINK" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/LINK/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y= json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
            # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True
    if "XTZ" in incoming_msg:
        r = requests.get("https://api.polygon.io/v1/open-close/crypto/XTZ/USD/2020-10-14?adjusted=true&apiKey=ndBi6VVwbpPf6l5SkUUsyJvwHX4R6sxG")
        if r.status_code == 200:
            y = json.loads(r)
            tex = 'OPEN :' + str(y["open"]) + '\n' + 'Close :' + str(y["close"])
            # tr = 'please type "hey" or "hi" or "menu" to view the options'
            response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True

    if not responded:
        msg.body("sorry i didnt get you , enter something valid or just enter hi or hey")
    return str(response)
if __name__ == "__main__":
    app.run()




















