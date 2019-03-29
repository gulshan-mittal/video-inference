# import env_setup
import cv2
import argparse
import os, sys


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--task", dest = 'TASK', default= 'ObjectDetection', help="Task to be Performed")
    args.add_argument("--network", dest = 'network', default= 'YOLOv3', help="Network to be used")
    args.add_argument("--input", dest = 'pathIn', help="path to video")
    args.add_argument("--output", dest = 'pathOut', help="path to output video")
    arg = args.parse_args()
    print(arg)
    if (arg.network == 'YOLOv3'):
    	os.system("python3 ./ObjectDetection/YOLOv3/object_detection_yolo.py --video=" + arg.pathIn + ' ' + '--output=' + arg.pathOut)
    elif (arg.network == 'Mask-RCNN'):
    	os.system("python3 ./ObjectDetection/Mask-RCNN/mask_rcnn.py --video=" + arg.pathIn + ' ' + '--output=' + arg.pathOut)