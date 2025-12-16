# import requests
# from datetime import datetime, timedelta
#
# API_URL = "https://ins..uz/api/Person/GetByPassportData"   # ← replace with your own legal API
# TOKEN = ""                                      # ← insert your own valid token
#
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "content-type": "application/json",
#     "authorization": f"Bearer {TOKEN}",
#     "lang": "uz-cyrl",
# }
#
# def date_range(start_date, end_date):
#     """Generate dates from start_date to end_date (datetime objects)."""
#     current = start_date
#     while current <= end_date:
#         yield current
#         current += timedelta(days=1)
#
# start = datetime.strptime("2007-02-21", "%Y-%m-%d")
# end   = datetime.strptime("2007-05-31", "%Y-%m-%d")  # example — change as needed
#
# for d in date_range(start, end):
#     body = {
#         "documentTypeId": 5,
#         "seria": "",
#         "number": "",
#         "dateOfBirth": d.strftime("%d.%m.%Y"),
#         "pinfl": "",
#         "cadastralNumber": "",
#         "includeAddress": True,
#         "includePhoto": True,
#     }
#
#     response = requests.post(API_URL, headers=headers, json=body)
#
#     print(d.strftime("%d.%m.%Y"), "→ HTTP", response.status_code)
#
#     if response.status_code == 200:
#         print("✔ Success on:", d.strftime("%d.%m.%Y"))
#         print("Response:", response.json())
#         break

#
# fruits = ['apple','banana','chery']
# fruits.insert('orange',1)