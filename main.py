import requests
from requests.auth import HTTPBasicAuth

url = "https://sandbox.test-simplexcc.com/wallet/merchant/v2/quote"
params = {"auth": "apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"}

response = requests.post(url, headers=({"Authorization":"apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                                                        ".eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"}))

print(response.content)
print("\n\nresult:")
print(response)
