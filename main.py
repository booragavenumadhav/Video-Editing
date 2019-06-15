#Comments are coming in next update
import cv2
from skimage.measure import compare_ssim
images=[]
vidObj=cv2.VideoCapture("onlyus.mp4")
success,old_image=vidObj.read()
grayA=cv2.cvtColor(old_image,cv2.COLOR_BGR2GRAY)
height,width,layers=old_image.shape
size=(width,height)
while True:
    success,image=vidObj.read()
    if not success:
        break
    grayB=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    score=compare_ssim(grayA,grayB)
    if(score<0.5):
        images.append(old_image)
        print("Working")
    grayA=grayB
    old_image=image
out=cv2.VideoWriter('out.avi',cv2.VideoWriter_fourcc(*'DIVX'),2,size)
for i in range(len(images)):
    out.write(images[i])
out.release()
