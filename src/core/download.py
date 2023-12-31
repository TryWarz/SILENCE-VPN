# mettre un ficher dans un zip linux est envoie le zip sur discord
import getpass
import zipfile
import requests

# create a zip file

class Zip:
    def __init__(self):
        pass

    def send(self, user, url):
        with zipfile.ZipFile(f"{user}.zip", "w") as zip:
            zip.write(f"{user}.ovpn")

        requests.post(url=url, files={"file": open(f"{user}.zip", "rb")})
        print("File send with success.")
    
