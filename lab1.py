import requests

#Print current version of requests
print("The current version is: ", requests.__version__)

#GET google homepage
hp = requests.get("http://www.google.com")
print(hp)

#This script on git hub
git_url = "https://raw.githubusercontent.com/DecKirin/CMPUT404LAB1/main/lab1.py"
source_code = requests.get(git_url)
print(source_code.text)
#Download the source code
download_file = open("downloaded_lab1_xiding.py","wb")
download_file.write(source_code.content)
download_file.close()