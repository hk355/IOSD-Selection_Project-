#IMPORT
import numpy as np
import cv2
import os
import argparse
from imutils import paths
#Hash function
def hash(image,hashsize=8) :
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	resized=cv2.resize(gray,(hashsize+1,hashsize))
	diff=resized[:,1:]>resized[:,:-1]
	return sum([2 ** i for(i,v) in enumerate(diff.flatten()) if v])

#argument parser to read files
ap=argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="path to input dataset")
args =vars(ap.parse_args())
print("computing image hashes")
imagePaths = list(paths.list_images(args["dataset"]))
#intialize dictionary for hashes
hashes={}
#compute hashes and store
for ip in imagePaths:
	image=cv2.imread(ip)
	h=hash(image)
	p=hashes.get(h,[])
	p.append(ip)
	hashes[h]=p

#loop over dictionary
for (h,hp) in hashes.items():
	if len(hp) > 1:
		for p in hp[1:] :
			os.remove(p)
		
	
	