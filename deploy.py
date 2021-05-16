from dotenv import dotenv_values
import requests

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
deployUrl = config["DEPLOY_URL"]
# print(depl)
with open('src.tar.gz', 'rb') as f:
    fileData = f.read()
# print(fileData)
s = fileData.decode('latin-1') 
# print(s)
data = { "data": s }

r = requests.post(deployUrl, json = data, params={"name": "gtts"})
print(r.text)
