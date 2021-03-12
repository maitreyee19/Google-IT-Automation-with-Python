from PIL import Image
from PIL import ImageFilter
import os
from os.path import isfile, join
def conver2Rgb(im):
    im = im.rotate(270)
    size = (128, 128)
    im = im.resize(size)
    #im = im.convert('RGB')
    return im


def main():
    # path of the folder containing the raw images
    inPath = "/home/bhabani/Work/GoogWeek1/"

    outPath = "/home/bhabani/Work/GoogWeek1/out/"

    onlyfiles = [f for f in os.listdir(inPath) if isfile(join(inPath, f))]
    print(onlyfiles)
    for img in onlyfiles:
        im = Image.open(join(inPath, img))
        try:
            im = conver2Rgb(im)
            img_name, ext = os.path.splitext(img)

            outfile = img_name + ".jpeg"

            im.save(join(outPath, outfile), "JPEG")
        except Exception as e:
            print(e)
        except:
            print("some error")






if __name__ == '__main__':
    main()
