import cv2
import math 
from PIL import Image
from sklearn.cluster import KMeans

img = cv2.imread('1.jpg') # Can be many different formats.
img_gray_mode = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

p = img_gray_mode.shape
print(p)
rows =img.shape[0]
cols = img.shape[1]

newList= []
for row in range(rows):  
   #newList.append([])
   for col in range(cols):
    newList.append([img_gray_mode[row][col]])
print(newList[0][0])
kmeans = KMeans(n_clusters=5).fit(newList)
centroids = kmeans.cluster_centers_
for row in range(rows):  
   #newList.append([])
   for col in range(cols):
     
     min=256
     for i in range(len(centroids)):
       
       y= img_gray_mode[row][col] -centroids[i]
       x=abs(y)
       if min>x:
            min=x
       img_gray_mode[row][col]=min
cv2.imwrite('1.jpg',img_gray_mode)