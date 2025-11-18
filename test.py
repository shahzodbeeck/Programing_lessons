import requests

response =requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
print(response.json())