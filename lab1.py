import requests

#Print current version of requests
print("The current version is: ", requests.__version__)

#GET google homepage
hp = requests.get("http://www.google.com")
print(hp)

