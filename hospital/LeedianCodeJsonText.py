# 生成ios 特征点代码 脚本
import os
import json
outPutPath=os.path.abspath('.')+'/imageName.json'
# with open('/hospital/image.json', encoding='utf-8') as f:
with open(os.path.abspath('.')+'/image.json', encoding='utf-8') as f:
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
