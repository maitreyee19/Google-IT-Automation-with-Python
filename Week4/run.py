#!/usr/bin/env python3
import os
from os.path import isfile, join
import json
import requests
import locale
def main():
    # path of the folder containing feedback
    inPath = "./supplier-data/descriptions/"
    textfiles = [f for f in os.listdir(inPath) if isfile(join(inPath, f))]


    for file in textfiles:
        dictForFeedback = {}

        try:
            with open(join(inPath, file), 'r') as f:
                Lines = f.readlines()
                dictForFeedback["name"] = Lines[0].rstrip()
                lbVal = Lines[1].replace(" lbs","")

                dictForFeedback["weight"] = int(lbVal.rstrip("\n"))
                dictForFeedback["description"] = Lines[2].rstrip()

                dictForFeedback["image_name"] = file.split(".")[0]+".jpeg"
                dataInJson = json.dumps(dictForFeedback)

                response = requests.post("http://34.71.239.21/fruits/", data=dataInJson,headers={"Content-Type":"application/json"})
                if not response.ok:
                    raise Exception("GET failed with status code {}".format(response.status_code))
        except Exception as e:
            print(e)
        except:
            print("the file with name {} failed .".format(file))


if __name__ == '__main__':
    main()

