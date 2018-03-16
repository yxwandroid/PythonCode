info = 'a-b!ca'
# print info.find('a')##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
#16
str="Leedian-1F-H-000-8.14"

# tempTag=str.index('!')
# print(str.index('!'))
# print(str.rfind("-"))
temp=str.rfind('-')

print(str[0:temp])


print(str[temp+1:])