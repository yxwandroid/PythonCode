import os
import  cv2
outPutPath=os.path.abspath('.')+'/logo.jpeg'
outPutPath1=os.path.abspath('.')+'/logo1.jpeg'
img = cv2.imread(outPutPath)
cv2.namedWindow("Image")
cv2.imshow("Image", img)

cv2.imwrite(outPutPath1, img)
cv2.waitKey (0)