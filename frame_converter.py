import env_setup
import cv2
import argparse


def extractImages(pathIn, pathOut):
	vidcap = cv2.VideoCapture(pathIn)
	success,image = vidcap.read()
	count = 0
	while success:
	  cv2.imwrite( pathOut + '/' +  "frame%d.png" % count, image)     # save frame as PNG file      
	  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))
	  success,image = vidcap.read()
	  print('Read a new frame: ', success)
	  count += 1

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--pathIn", dest = 'pathIn', help="path to video")
    args.add_argument("--pathOut", dest = 'pathOut', help="path to images")
    arg = args.parse_args()
    print(arg)
    extractImages(arg.pathIn, arg.pathOut)
