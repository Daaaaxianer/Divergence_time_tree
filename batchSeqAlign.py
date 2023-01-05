# -*- coding:utf-8 -*-
# @FileName :batchSeqAlign.py
# @Time     :2022/2/9 16:04
# @Author   :Xian

## Perform multiple sequence alignment of single-copy gene sequences
## 批量完成单拷贝基因序列的多序列比对，muscle v5 生成的fasta比对格式
## 脚本使用顺序  extractSingleCopySequence.py --> batchId2Spname.py --> batchSeqAlign.py --> fasAlign2phy.py -->delStopCodon.py
import os
import shutil
import argparse
import time

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
    parser = argparse.ArgumentParser(description = "用途：读取名称替换后的单拷贝基因序列，执行多序列比对。")
    parser.add_argument("scpdir", type = str, help = "dir of singleCopySeq (type = str)")
    parser.add_argument("-r","--rscpsuffix", type = str, default = "fasta", help = "suffix of replaced singleCopySeq(type = str)")
    args = parser.parse_args()

    print(args.scpdir,args.rscpsuffix)

    name = getFile(args.scpdir, f'.{args.rscpsuffix}')

    for id in name:
        print(f'\nReading {args.scpdir}/{id}')        
        os.system(f'muscle -in {args.scpdir}/{id} -out {args.scpdir}/{id}.fas')
        # os.popen(f'muscle -in {args.scpdir}/{id} -out {args.scpdir}/{id}.fas')
        # time.sleep(5)
        # os.popen在循环中是多线程异步执行，如果每个线程执行时间很长会发生相互干扰，但是效率更高。需要合理利用

        # os.popen("muscle -in ./singleCopySeq/"+id+" -fastaout ./singleCopySeq/"+id+".fas")
        # os.popen("cat ./singleCopySeq/*.phy >> ./singleCopySeq/all.phy")
        # shutil.copy("./singleCopySeq/*.phy", "./singleCopySeq/all.phy")