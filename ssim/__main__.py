import argparse
import ssim
from ssim.compat import Image
import os, sys

def main():
    parser = argparse.ArgumentParser(prog="pyssim",
                                     description="Compares two images using the SSIM metric")
    parser.add_argument('original_dir')
    parser.add_argument('comparison_dir')
    args = parser.parse_args()

    original_dir=args.original_dir
    compare_dir=args.comparison_dir

    for i in range(1, 6000):
		im1 = Image.open(args.original_dir+str(i)+".png")
		im2=Image.open(args.comparison_dir+str(i)+".png")
		ssim_value=ssim.compute_ssim(im1, im2);
		print "SSIM for Image #", i, ": ", ssim_value

    
if __name__ == '__main__':
    main()
