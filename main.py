import json
import requests

url = "https://sandbox.test-simplexcc.com/wallet/merchant/v2/quote"
autherize = "apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"

req_amount = 0.005
req_currency = "BTC"
req_fiat = "EUR"
digit_curreny = "BTC"
end_user = "febaaf91-2c44-4f1a-b02c-8fafe25e75a2"
payment_methods = ["credit_card"]

credit_num = "4711 1000 0000 0000"
exp_date = "05/24"
code = "123"


def bittoeuro():
    req_amount = 0.005
    req_currency = "BTC"
    req_fiat = "EUR"
    digit_curreny = "BTC"
    response = requests.post(url, headers=({"Authorization": autherize}), json=(
        {"requested_amount": req_amount, "requested_currency": req_currency, "fiat_currency": req_fiat,
         "digital_currency": digit_curreny, "end_user_id": end_user, "payment_methods": payment_methods}))
    read = response.json()
    print(json.dumps(read, indent=4, sort_keys=True))


def dollartobit():
    req_amount = 950
    req_currency = "USD"
    req_fiat = "USD"
    digit_curreny = "BTC"
    response = requests.post(url, headers=({"Authorization": autherize}), json=(
        {"requested_amount": req_amount, "requested_currency": req_currency, "fiat_currency": req_fiat,
         "digital_currency": digit_curreny, "end_user_id": end_user, "payment_methods": payment_methods}))
    read = response.json()
    print(json.dumps(read, indent=4, sort_keys=True))


def paymentrequest():
    url = "https://sandbox.test-simplexcc.com/wallet/merchant/v2/payments/partner/data"
    qoute_num = "b95d0711-9f3d-4013-ac4f-89f18474fd25"
    payment_num = "c3044f5b-9d61-45d5-b216-b32b57a51244"
    acc_details = {
        "account_details": {
            "app_provider_id": "wallex",
            "app_end_user_id" : end_user,
            "app_version_id" : "1.3.1",
            "signup_login" : {
                "ip" : "212.179.111.110",
                "timestamp" : "2022-01-15T09:27:34.431Z"
            }
        },
        "transaction_details": {
            "payment_details": {
                "quote_id": qoute_num,
                "payment_id": payment_num,
                "destination_wallet": {
                    "address" : "16HAsVHRcmGSxGHfFvq67zjQq8XjEQFvVr",
                    "currency" : "BTC"
                }
            }

        }

    }


    test = acc_details
    response = requests.post(url, headers=({"Authorization": autherize}), json=test)
    testing = response.json()
    print(json.dumps(testing, indent=4, sort_keys=True))


bittoeuro()
print("\n\n\n")
dollartobit()
print("\n\n\n")
paymentrequest()
print("\n\n\n")
