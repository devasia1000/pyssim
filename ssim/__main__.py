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

    base_images=os.listdir(base_dir)
    compare_images=os.listdir(compare_dir)

    base_images.sort()
    compare_images.sort()
    
    try:
	#assert(len(base_images)==len(compare_images))
	pass
    except:
	print "number of image files mismatch"
	print base_dir, ": ", len(base_images)," ", compare_dir, ": ", len(compare_images)
	sys.exit(0)

    for i in range(len(base_images)):
    	im1 = Image.open(args.base_dir+"/"+base_images[i])
    	im2 = Image.open(args.comparison_dir+"/"+compare_images[i])
    	print "SSIM for Image #", i, ": ", ssim.compute_ssim(im1, im2)
    
if __name__ == '__main__':
    main()
