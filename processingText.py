import os
from os.path import isfile, join
import requests


# def conver2Rgb(im):
#     im = im.rotate(270)
#     size = (128, 128)
#     im = im.resize(size)
#     #im = im.convert('RGB')
#     return im


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
                response = requests.post("https://example.com/path/to/api", data=dictForFeedback)
                if not response.ok:
                    raise Exception("GET failed with status code {}".format(response.status_code))
        except Exception as e:
            print(e)
        except:
            print("the file with name {} failed .".format(file))


if __name__ == '__main__':
    main()
