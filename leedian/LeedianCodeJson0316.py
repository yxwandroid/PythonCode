# 生成ios 特征点代码 脚本
import os
import json
# outPutPath='/Users/yangxuewu/Desktop/imageNameleedian.json'
outPutPath=os.path.abspath('.')+'/imageNameleedian.json'


def getFileName():
    theList = []
    # 选择名字中需要保留的部分
    # new_name =name
    # os.rename(file, new_name)
    # os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    for file in os.listdir('/Users/yangxuewu/Desktop/Assets.xcassets'):
        if file[-2:] == 'py':
            continue  # 过滤掉改名的.py文件
            # 去掉空格
        name = file.replace('.arreferenceimage', '')
        theList.append(name)
        # print(name)

    return theList


def getCreatCode(item):
    with open(os.path.abspath('.') + '/imageleedian.json', encoding='utf-8') as f:
        line = f.read()
        jsonStr = json.loads(line)
        new = []

        for user in jsonStr:
            itemName = item[0:13]
            if itemName == user['filename']:
            #    tempFileName = user['filename'] + str(a)
                outPutTxt = "checkPointsDic[\"" + item + "\"] = PlanCheckPoint(x: " + user[
                    'x'] + ", y: 0, z: " + user['y'] + ", layerId:\"" + user['layerId'] + "\");"
                file_object = open(outPutPath, 'a')
                file_object.write("\n" + outPutTxt)
                file_object.close()
                print(outPutTxt)

        f.close()

fileNameList = getFileName()
for item in fileNameList:
    getCreatCode(item)


# getCreatCode()



# checkPointsDic["leedian-1F-MO-1"] = PlanCheckPoint(x: 07015, y: 0, z: 10714, layerId:"273773484848499392828");
# checkPointsDic["Leedian-1F-B-5"] = PlanCheckPoint(x: 10597, y: 0, z: 2289, layerId:"d1a0d30f-d918-47bb-977b-8f2ec96ecff4");









