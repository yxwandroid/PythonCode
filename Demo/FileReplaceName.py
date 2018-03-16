import os;
# os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
for file in os.listdir('/Users/yangxuewu/Desktop/Assets.xcassets'):
    if file[-2:] == 'py':
        continue  # 过滤掉改名的.py文件
        # 去掉空格
   # name = file.replace('arreferenceimage.image', 'arreferenceimage')
    print(file)
    # 选择名字中需要保留的部分
    # new_name =name
    # os.rename(file, new_name)
