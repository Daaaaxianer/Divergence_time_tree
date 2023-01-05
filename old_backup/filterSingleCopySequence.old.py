# -*- coding:utf-8 -*-
# @FileName :filterSingleCopySequence.py
# @Time     :2022/2/9 9:42
# @Author   :Xian

## 1.从orthfinder结果中提取单拷贝基因
## 2.对每组单拷贝基因进行序列比对
## 脚本使用顺序 filterSingleCopySequence.py --> batchFileRename.py --> batchFile2Phy.py --> phylipConvert.py -->deleteStopCodon.py

import re
import os
import shutil
from Bio.Seq import Seq
from Bio import SeqIO

def filterId (Orthsco,Orth):
    '''
    Orthsco : Orthfiner file Orthogroups_SingleCopyOrthologues.txt
    Orth : Orthfiner file Orthogroups.txt
    '''
    orthSingleList = []
    with open(Orthsco) as afile:
        for line in afile:
            line = line.strip()
            orthSingleList.append(line)
        print(orthSingleList)
    orth2single = {}
    with open(Orth) as bfile:
        for line in bfile:
            line = line.strip()
            lineList = re.split('[:]',line)
            orth2single[lineList[0]] = lineList[1]
        print(orth2single)
    return orthSingleList,orth2single

def id2Fa (allFasta):
    id2seq = {}
    for seq_record in SeqIO.parse(allFasta, "fasta"):
        id2seq[seq_record.id] = seq_record
    return id2seq

if __name__ == '__main__' :
    osinglelist,o2single = filterId("Orthogroups_SingleCopyOrthologues.txt","Orthogroups.txt")
    id2seq = id2Fa("all.cds.fasta")
    if os.path.exists("singleCopySeq"):
        shutil.rmtree("singleCopySeq")
    os.mkdir("singleCopySeq")
    for og in osinglelist:
        # print(o2single[og])
        idList = re.split('\s+', o2single[og])[1:] ### delete blank in head
        seqList = []
        for id in idList:
            print (og+' '+id)
            seqList.append(id2seq[id])
        SeqIO.write(seqList, "./singleCopySeq/"+og + ".singlecopy.cds.fa", "fasta")