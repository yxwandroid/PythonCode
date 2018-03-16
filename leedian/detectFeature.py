# (!/usr/bin/python)
#coding:utf8  
  
import os  
import cv2  
import shutil
import sys
import numpy as np  



size = len(sys.argv)
if size != 5:
    print("参数传递错误")
    print ("python detectFeature.py srcFolder successFolder faildFolder num")
    sys.exit()

orb = cv2.ORB_create(500)

def detectFeatrure(file):
    img1 = cv2.imread(file)
    kp, des = orb.detectAndCompute(img1,None)
    return len(kp)

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径      
        shutil.copyfile(srcfile,dstfile)      #复制文件
       
        
def dirlist(path, allfile): 
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:             
            allfile.append(filepath)   
            num = int(sys.argv[4])       
            if detectFeatrure(filepath) > num : 
                destFile = filepath.replace(sys.argv[1],sys.argv[2],1)                                
                mycopyfile(filepath,destFile)
            else:
                destFile = filepath.replace(sys.argv[1],sys.argv[3],1)                                
                mycopyfile(filepath,destFile)


    return allfile  
  
dirlist(sys.argv[1], [])  
print ("Success!")