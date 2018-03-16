import os
import json
import shutil
import sys
outPut = '/Users/yangxuewu/Desktop/Assets.xcassets/'
inPut ="/Users/yangxuewu/Desktop/3014leedian/data"
outPutPath = os.path.abspath('.') + '/imageNameleedian.json'   # 生成代码文件
# 遍历文件夹
def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if fi=='.DS_Store':
            continue
        if os.path.isdir(fi_d):  # 若是文件夹 就递归遍历
            gci(fi_d)
        else:
          #  print(fi_d)
            getFeatureImage(fi_d)







# Assets.xcassets
# 创建文件夹保存图片
def getFeatureImage(filepath):

    imageName = filepath.split("/")[-1]  # 图片的名称

    temp = imageName.rfind('-')
    tempStr = imageName[0:temp]
    tempNum=imageName[temp+1:].replace('.jpg','')
    fileName = tempStr+"-"+tempNum.replace('.','')
    filePathName = outPut + fileName + '.arreferenceimage'


    if os.path.exists(filePathName) == False:
        os.mkdir(filePathName)  # 创建目录

    # 图片文件的copy
    shutil.copyfile(filepath, filePathName + "/" + fileName + ".jpg")
    #print('----------'+filePathName+'--------------'+str(tempNum))
    imageJson = {
        "images": [
            {
                "idiom": "universal",
                "filename": fileName+'.jpg'
            }
        ],
        "info": {
            "version": 1,
            "author": "xcode"
        },
        "properties": {
            "width": float(tempNum),
            # "unit": "inches"
        }
    }
    with open(filePathName + "/Contents.json", "w") as f:
       json.dump(imageJson, f, ensure_ascii=False,indent=4)

gci(inPut)
print('批量生成文件成功')

