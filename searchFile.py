import os

#os.walk函数用于遍历目录下所有文件

matches=[]
filePath=r"f:\code"
#搜索指定路径下py文件中含有指定关键字的文件
for (dirname,dirshere,fileshere) in os.walk(filePath):
    for filename in fileshere:
        if filename.endswith(".py"):
            pathname=os.path.join(dirname,filename)
            if "filePath" in open(pathname,"r",encoding="utf-8").read():
                matches.append(pathname)
print(matches)