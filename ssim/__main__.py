import argparse
import ssim
from ssim.compat import Image
import os, sys

def main():
    parser = argparse.ArgumentParser(prog="pyssim",
                                     description="Compares two images using the SSIM metric")
    parser.add_argument('base_dir')
    parser.add_argument('comparison_dir')
    args = parser.parse_args()

    base_dir=args.base_dir
    compare_dir=args.comparison_dir

    for i in range(1, 10001):
#        try:
    	    im1 = Image.open(args.base_dir+str(i)+".png")
    	    im2 = Image.open(args.comparison_dir+str(i)+".png")
    	    print "SSIM for Image #", i, ": ", ssim.compute_ssim(im1, im2)
 #       except:
#	    print "Error processing Image # ", i, ". File", args.base_dir+str(i)+str(".png"), "or", args.comparison_dir+str(i)+str(".png"), "does not exist!"
    
if __name__ == '__main__':
    main()
