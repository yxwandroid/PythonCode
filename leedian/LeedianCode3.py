import os
import json
import shutil


# 最新版本

theList = ['00', '01', '02', '11', '12', '13']
#tempList = ['0', '1', '2', '3', '4', '5']


# 遍历文件夹
def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):  # 若是文件夹 就递归遍历
            # print(os.path.join(filepath, fi_d))
            gci(fi_d)
        else:
            imageNameqq = fi_d.split("/")[-1]
            temp = imageNameqq.rfind('-')
            tempStr=imageNameqq[0:temp]
            # print(str[0:temp])
            imageName = tempStr[-2:]
            if imageName in theList:
                getFeatureImage(os.path.join(filepath, fi_d))
                #   print("------"+fi_d+"------" + imageName)

                # print(os.path.join(filepath,fi_d))#递归遍历/root目录下所有文件


outPut = '/Users/yangxuewu/Desktop/Assets.xcassets/'


# Assets.xcassets
# 创建文件夹保存图片
def getFeatureImage(filepath):
    # 图片的名称
    imageName = filepath.split("/")[-1]

    temp = imageName.rfind('-')
    tempStr = imageName[0:temp]
    tempNum=imageName[temp+1:].replace('.jpg','')

    tempNumName=round(float(tempNum), 2)
  #  print(tempNumName)
    suffix = tempStr[-3:]

    #suffix = imageName[-7:-4]


    # imageNameTemp=imageName.replace('.jpg','')
    # imageNameTemp=tempStr+"-"+str(tempNumName)
    imageNameTemp=tempStr
    fileName=''
    if suffix == '000':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '0')
        print('----' + fileName)
    elif suffix == '001':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '1')
        print('----' + fileName)
    elif suffix == '002':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '2')
        print('----' + fileName)
    elif suffix == '011':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '3')
        print('----' + fileName)
    elif suffix == '012':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '4')
        print('----' + fileName)
    elif suffix == '013':
        # print('----' + suffix)
        fileName = imageNameTemp.replace(suffix, '5')
        print('----' + fileName)

    # w文件夹的名称
    # fileName = imageName.replace('.jpg', '')
    # 文件夹的路径
    filePathName = outPut + fileName + '.arreferenceimage'

    # print(filePathName)
    # 创建文件夹逻辑
    if os.path.exists(filePathName) == False:
        os.mkdir(filePathName)  # 创建目录

    # 图片文件的copy
    shutil.copyfile(filepath, filePathName + "/" + fileName + ".jpg")

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

gci("/Users/yangxuewu/Desktop/0315leedian")

