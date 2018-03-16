# 文件的读写


# try:
#     f = open('read.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#

#
# with open('read.txt', 'r') as fileReader:
#     print(fileReader.read())
#
#
# with open('read.txt', 'r') as fileReader:
#     for line in fileReader.readlines():
#         print(line.strip())

#
# with open('read.txt', 'w') as fileWriter:
#     for num in range(1, 100):
#         fileWriter.write(str(num)+'\n')