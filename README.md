# pyssim

This module implements the Structural Similarity Image Metric (SSIM). Original code written by Antoine Vacavant from http://isit.u-clermont1.fr/~anvacava/code.html, with modifications by Christopher Godfrey, Jeff Terrace and Devasia Manuel 

## Prereqs

A video should be decomposed into image files with ffmpeg before running this tool:

    $ ffmpeg -i <pathToVideo> -f image2 %d.png
    
Image files for seperate videos should be stored in seperate directories, these directories can be passed to pyssim to calculate the SSIM for each frame of video

## Installation

    pip install pyssim

## Running

##Method 1
    $ pyssim --help
    usage: pyssim [-h] path_to_dir1 path_to_dir2
    ##NOTE: path_to_dir1 and path_to_dir2 should not include the trailing backslash

    Compares two directories of images using the SSIM metric

##Method 2
    python ./ssim/__main__.py path_to_dir1 path_to_dir2
 
    ##NOTE: path_to_dir1 and path_to_dir2 should not include the trailing backslash
    
    Compares two directories of images using the SSIM metric

## References

* [1] Z. Wang, A. C. Bovik, H. R. Sheikh and E. P. Simoncelli. Image quality assessment: From error visibility to structural similarity. IEEE Transactions on Image Processing, 13(4):600--612, 2004. 
* [2] Z. Wang and A. C. Bovik. Mean squared error: Love it or leave it? - A new look at signal fidelity measures. IEEE Signal Processing Magazine, 26(1):98--117, 2009.
