
import os
from os.path import isfile, join
import requests
def main():
    # path of the folder containing feedback
    inPath = "/home/bhabani/Work/googleITAutomation/week2"
    textfiles = [f for f in os.listdir(inPath) if isfile(join(inPath, f))]
    dictForFeedback = {}
    for file in textfiles:
        try:
            with open(join(inPath, file), 'r') as f:
                Lines = f.readlines()
                dictForFeedback["title"] = Lines[0].rstrip()
                dictForFeedback["name"] = Lines[1].rstrip()
                dictForFeedback["date"] = Lines[2].rstrip()
                dictForFeedback["feedback"] = Lines[3].rstrip()
                data ={"title": "Great Customer Service", "date": "2017-12-21", "name": "John", "feedback": "The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!"}
                response = requests.post("http://http://34.123.139.34/feedback", data=data)
                if not response.ok:
                    raise Exception("GET failed with status code {}".format(response.status_code))
        except Exception as e:
            print(e)
        except:
            print("the file with name {} failed .".format(file))


if __name__ == '__main__':
    main()

