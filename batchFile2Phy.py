# -*- coding:utf-8 -*-
# @FileName :batchFile2Phy.py
# @Time     :2022/2/9 16:04
# @Author   :Xian

## 多序列比对单拷贝基因序列，生成phylip格式，并合并为一个phylip文件，作为mcmctree输入文件之一
## 脚本使用顺序 filterSingleCopySequence.py --> batchFileRename.py --> batchFile2Phy.py --> phylipConvert.py -->deleteStopCodon.py
import os
import shutil

def getFile(pathname,suffix): ###
    name = []
    for root, dirs, files in os.walk(pathname):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files同样是list, 内容是该文件夹中所有的文件(不包括子目录)
        for i in files:
            # print (i)
            if os.path.splitext(i)[1] == suffix:
                name.append(i)
    print (name)
    return name

if __name__ == '__main__':
    name = getFile("./singleCopySeq",".fasta")
    for id in name:
        # print(id)
        os.popen("muscle -in ./singleCopySeq/"+id+" -fastaout ./singleCopySeq/"+id+".fas")
        # os.popen("cat ./singleCopySeq/*.phy >> ./singleCopySeq/all.phy")
        # shutil.copy("./singleCopySeq/*.phy", "./singleCopySeq/all.phy")