#Importing required packages
import cv2
from skimage.measure import compare_ssim
images=[]
source_file="onlyus.mp4"
dest_file='out.mp4'
video_format=cv2.VideoWriter_fourcc(*'DIVX')
fps=2
vidObj=cv2.VideoCapture(source_file) #reading the video path
success,old_image=vidObj.read() #Getting a frame from the video
grayA=cv2.cvtColor(old_image,cv2.COLOR_BGR2GRAY) # Converting the frame into gray for easier calculation
height,width,layers=old_image.shape
size=(width,height)
while True:
    success,image=vidObj.read()
    if not success:
        break
    grayB=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    score=compare_ssim(grayA,grayB) # comparing two frames
    if(score<0.5):
        images.append(old_image)
    grayA=grayB
    old_image=image
out=cv2.VideoWriter(dest_file,video_format,fps,size)
for i in range(len(images)):
    out.write(images[i])
out.release()
