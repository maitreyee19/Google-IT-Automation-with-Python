#!/usr/bin/env python3
import requests
import os
from os.path import isfile, join
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
inPath = "./supplier-data/images/"
imgFiles = [f for f in os.listdir(inPath) if isfile(join(inPath, f) )]
print(imgFiles)

for imgName in imgFiles:
    if imgName.endswith(".jpeg"):


        try:

            with open(join(inPath, imgName), 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                if not r.ok:
                    raise Exception("GET failed with status code {}".format(r.status_code))
        except Exception as e:
            print(e)


