# -*- coding:utf-8 -*-
# @FileName :batchId2SpName.py
# @Time     :2022/2/9 17:46
# @Author   :Xian

## Modify the gene name in the single copy sequence to the species name
## 批量修改单拷贝序列中基因名字为物种名，方便后续多序列比对(phylip格式)
## 脚本使用顺序 extractSingleCopySequence.py --> batchId2Spname.py --> batchSeqAlign.py --> fasAlign2phy.py -->delStopCodon.py

import re
import os
import shutil
from Bio import SeqIO
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

def fas2phy(infas):
    with open(infas, 'r') as fin:
        sequences = [(m.group(1), ''.join(m.group(2).split()))
                     for m in re.finditer(r'(?m)^>([^ \n]+)[^\n]*([^>]*)', fin.read())]
        with open(infas+".phy", 'w') as fout:
            fout.write('%d %d\n' % (len(sequences), len(sequences[0][1])))
            for item in sequences:
                fout.write('%-20s %s\n' % item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "用途：利用原始cds中序列与文件名(物种名)的索引关系，修改单拷贝基因序列名称为物种名。")
    parser.add_argument("cdsdir", type = str, help = "dir of xxx.cds.fa file, xxx is specie's name (type = str)") 
    parser.add_argument("-c","--cdssuffix", type = str, default = "fa", help = "suffix of xxx.cds.fa(type = str)")
    parser.add_argument("scpdir", type = str, help = "dir of singleCopySeq (type = str)")
    parser.add_argument("-s","--scpsuffix", type = str, default = "fa", help = "suffix of singleCopySeq, It is recommended to use a non-fasta suffix such as 'fa' to avoid errors in subsequent programs (type = str)")

    args = parser.parse_args()

    ## Read cds files to establish the index relationship between the sequence and the file name (species name)
    ## 读取CDS文件，建立序列与文件名(物种名)的索引关系
    cdsFa = getFile(args.cdsdir,f'.{args.cdssuffix}')
    print(cdsFa)
    id2sp = {}
    for sp in cdsFa:
        print ("input "+ sp +"\n")
        spName = re.split(r"\.",sp)
        for seq_record in SeqIO.parse(args.cdsdir+'/'+sp,"fasta"):
            # print(seq_record)
            id2sp[seq_record.id] = spName[0]

    ## Read the single copy gene sequence and replace the gene name as the species name.
    ## 读取单拷贝基因序列，并将基因名称替换为物种名称。
    name = getFile(args.scpdir,f'.{args.scpsuffix}')
    for id in name:
        print (id)
        seqList = []
        for seq_record in SeqIO.parse(args.scpdir+'/'+id,"fasta"):
            seq_record.id = id2sp[seq_record.id]
            seq_record.description = seq_record.id
            seqList.append(seq_record)
        SeqIO.write(seqList, args.scpdir+'/'+id+"sta", "fasta")
