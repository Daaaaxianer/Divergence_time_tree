# -*- coding:utf-8 -*-
# @FileName :extractSingleCopySequence.py
# @Time     :2022/2/9 9:42
# @Author   :Xian

## 利用orthfinder结果及原始cds序列，提取单拷贝基因序列
## Extraction of single copy gene sequence
## 脚本使用顺序 extractSingleCopySequence.py --> batchId2Spname.py --> batchSeqAlign.py --> fasAlign2phy.py -->delStopCodon.py

import re
import os
import shutil
from Bio.Seq import Seq
from Bio import SeqIO
import argparse

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
    parser = argparse.ArgumentParser(description = "用途：提取Orthogroups.txt中的单拷贝基因序列，并对每组单拷贝基因进行序列比对。")
    parser.add_argument("oscgroups", type = str, help = "Orthfinder resulte file: \"Orthogroups_SingleCopyOrthologues.txt\" (type = str)") 
    parser.add_argument("ogroups", type = str, help = "Orthfinder resulte file: \"Orthogroups.txt\" (type = str)")
    parser.add_argument("allcds", type = str, help = "a merged coding squence file of all used species (type = str)")
    args = parser.parse_args()

    osinglelist,o2single = filterId(args.oscgroups, args.ogroups)
    id2seq = id2Fa(args.allcds)
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