#!/usr/bin/python  
#coding:utf8  
  
import os  
import cv2  
import shutil
import sys
import numpy as np  



size = len(sys.argv)
if size != 5:
    print ("参数传递错误")
    print ("python detectFeature.py srcFolder successFolder faildFolder num")
    sys.exit()

orb = cv2.ORB_create(500)

upbody = cv2.CascadeClassifier('haarcascade_upperbody.xml')
facealt = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')


def detectFeatrure(file):
    img = cv2.imread(file,0)
    count = detectBody(img)
    if count > 0:
        return 0
    kp, des = orb.detectAndCompute(img,None)    
    return len(kp)


def detectBody(img):
    count = len(upbody.detectMultiScale(img,1.3,5))
    count += len(facealt.detectMultiScale(img,1.3,5))
    return count    

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径      
        shutil.copyfile(srcfile,dstfile)      #复制文件
       
        
def dirlist(path): 
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath)  
        else: 
            print (filepath)
            num = int(sys.argv[4])       
            if detectFeatrure(filepath) > num : 
                destFile = filepath.replace(sys.argv[1],sys.argv[2],1)                                
                mycopyfile(filepath,destFile)
            else:             
                destFile = filepath.replace(sys.argv[1],sys.argv[3],1)                                
                mycopyfile(filepath,destFile)
 
  
dirlist(sys.argv[1])  
print ("Success!")