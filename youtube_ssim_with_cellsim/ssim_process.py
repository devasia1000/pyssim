import fileinput
from os.path import expanduser

ssim_1080p=dict() 
ssim_720p=dict()
ssim_480p=dict()
ssim_360p=dict()
ssim_240p=dict()
ssim_144p=dict()

def readFile(fil, dic):
    for line in fil:
        line=line.rstrip()
        sp=line.split(" : ")
        sp[0]=sp[0].replace("SSIM for Image # ", "")
        dic[str(sp[0])]=str(sp[1].strip())

def readSSIM():
    file_1080p=open(expanduser("~")+"/pyssim/data/youtube_1080p_ssim.txt")
    readFile(file_1080p, ssim_1080p)
    file_720p=open(expanduser("~")+"/pyssim/data/youtube_720p_ssim.txt")
    readFile(file_720p, ssim_720p)
    file_480p=open(expanduser("~")+"/pyssim/data/youtube_480p_ssim.txt")
    readFile(file_480p, ssim_480p)
    file_360p=open(expanduser("~")+"/pyssim/data/youtube_360p_ssim.txt")
    readFile(file_360p, ssim_360p)
    file_240p=open(expanduser("~")+"/pyssim/data/youtube_240p_ssim.txt")
    readFile(file_240p, ssim_240p)
    file_144p=open(expanduser("~")+"/pyssim/data/youtube_144p_ssim.txt")
    readFile(file_144p, ssim_144p)

    




stream={"2.0736e+06": ssim_1080p, "921600": ssim_720p, "409920": ssim_480p, "230400": ssim_360p, "102240": ssim_240p, "36864": ssim_144p}
 
readSSIM()

for line in fileinput.input():
    line=line.rstrip().strip()    
    sp=line.split(",")
    frame_count=sp[0].split(":")[1]
    video_resolution=sp[1].split(":")[1]
    
    print "SSIM for Frame #", frame_count, "of resolution", video_resolution, ":", stream[video_resolution][frame_count]
    
