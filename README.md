# pyssim

This module implements the Structural Similarity Image Metric (SSIM). Original code written by Antoine Vacavant from http://isit.u-clermont1.fr/~anvacava/code.html, with modifications by Christopher Godfrey, Jeff Terrace and Devasia Manuel 

This code can be used to generate SSIM graphs for MIT's Alfalfa project

## Prereqs

1) Latest version of Google Chrome
2) Original Charades video


## Running

##Generating SSIM Graphs

1) Download each of the video streams by going through the following substeps:

a) Open http://www.youtube.com/watch?v=wcLDdwPF9WM with Chromium make sure the video is playing in HTML5
b) Press 'F12' to bring up Chromium's webpage debugger, click on 'Network' - you should see all the GET requests
c) While the video is playing, manually change the quality level
d) Wait a few seconds for the video to change quality
e) Once you've noticed a change in quality, go to the network debugger and click         on the most recent 'videoplayback' in the left hand panel. The right hand panel             of the debugger should change.
f)  Go to the right hand panel of the debugger and click on 'Headers' and take note of the MIME type, it could be 'audio/mp4' for the audio stream and 'video/mp4' for a video stream. To download the stream, copy the request URL. 
g) Paste the link in the URL bar of a new tab, change the initial range parameter to 0 and the final range parameter to an arbitrarily large number. Press enter.
h) Right click on the video player that pops up and click on 'Save As'
i) Save your video to file (this step will take a very long time since YouTube will be throttling the bandwidth)

2) For each downloaded video stream, split the video into image files by running: mplayer -vo png:outdir=<imageOutputDir>,z=0 <inputVideoFile>

4) Change dir to the image output directory and run this script to resize images to 1920x1080: ls | perl -e 'while($in=<STDIN>){chomp($in); @arr=split("\\.", $in); $int=int($arr[0]); `mv ${in} ${int}.png`; `ffmpeg -i ${int}.png -vf scale=1920:1080 ${int}.png`;}' 

5) Clone pyssim from Github by running: git clone https://github.com/devasia1000/pyssim 

6) Run pyssim to calculate SSIM data: python ./pyssim/ssim/__main__.py <originalImageDir> <youtubeImageDir> >> ~/<outputFIle>

7) Use a tool of your choice (GNUPlot, Calc, XPlot, etc) to process the data and create fancy graphs

#Method 1
    $ pyssim --help
    usage: pyssim [-h] path_to_dir1 path_to_dir2
    ##NOTE: path_to_dir1 and path_to_dir2 should NOT include the trailing backslash

    Compares two directories of images using the SSIM metric

##Method 2
    python ./ssim/__main__.py path_to_dir1 path_to_dir2
 
    ##NOTE: path_to_dir1 and path_to_dir2 should not include the trailing backslash
    
    Compares two directories of images using the SSIM metric

## References

* [1] Z. Wang, A. C. Bovik, H. R. Sheikh and E. P. Simoncelli. Image quality assessment: From error visibility to structural similarity. IEEE Transactions on Image Processing, 13(4):600--612, 2004. 
* [2] Z. Wang and A. C. Bovik. Mean squared error: Love it or leave it? - A new look at signal fidelity measures. IEEE Signal Processing Magazine, 26(1):98--117, 2009.
