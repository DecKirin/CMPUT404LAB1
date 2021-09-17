import requests

print("The current version is: ", requests.__version__)

hp = requests.get("http://google.com")
print(hp)

