# 生成ios 特征点代码 脚本
import os
import json
# outPutPath='/Users/yangxuewu/Desktop/imageNameleedian.json'
outPutPath=os.path.abspath('.')+'/imageNameleedian.json'

with open(os.path.abspath('.')+'/imageleedian.json', encoding='utf-8') as f:
    line = f.read()
    jsonStr = json.loads(line)
    new = []
    for user in jsonStr:

        for a in range(6):
          tempFileName=user['filename']+str(a)
          outPutTxt="checkPointsDic[\""+tempFileName+"\"] = PlanCheckPoint(x: "+user['x']+", y: 0, z: "+user['y']+", layerId:\""+user['layerId']+"\");"
          file_object = open(outPutPath, 'a')
          file_object.write("\n"+outPutTxt)
          file_object.close()
          print(outPutTxt)


    f.close()



# checkPointsDic["leedian-1F-MO-1"] = PlanCheckPoint(x: 07015, y: 0, z: 10714, layerId:"273773484848499392828");
# checkPointsDic["Leedian-1F-B-5"] = PlanCheckPoint(x: 10597, y: 0, z: 2289, layerId:"d1a0d30f-d918-47bb-977b-8f2ec96ecff4");




#
#
# outPutPath='/Users/yangxuewu/Desktop/imageName.json'
#
# file_object = open(outPutPath, 'w')
#file_object.write('112')
# file_object.close( )
# for i in range(len(listImagePoint)):
#
#
#     print(i, listImagePoint[i])
#
#
#
#
#
