# 生成ios 特征点代码 脚本

import json
outPutPath='/Users/yangxuewu/Desktop/imageName.json'
with open('/Users/yangxuewu/Desktop/image.json', encoding='utf-8') as f:
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

