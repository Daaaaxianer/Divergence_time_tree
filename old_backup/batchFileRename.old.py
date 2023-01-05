# -*- coding:utf-8 -*-
# @FileName :batchFileRename.py
# @Time     :2022/2/9 17:46
# @Author   :Xian

## 修改单拷贝序列中基因名字为物种名，方面后面生成phylip格式
## 脚本使用顺序 filterSingleCopySequence.py --> batchFileRename.py --> batchFile2Phy.py --> phylipConvert.py -->deleteStopCodon.py

import re
from batchFile2Phy import getFile
from Bio import SeqIO

if __name__ == '__main__':
    name = getFile("./singleCopySeq",".fa")
    for id in name:
        print (id)
        seqList = []
        for seq_record in SeqIO.parse("./singleCopySeq/"+id,"fasta"):
            if(re.match('^Ca\d{2}g',seq_record.id)):
                seq_record.id = "Cannuum"
            if(re.match('^C\d{3}N',seq_record.id)):
                seq_record.id = "Caustralis"
            if (re.match('^Cp_v0.1', seq_record.id)):
                seq_record.id = "Ccampestri"
            if (re.match('^cc\d{2}g', seq_record.id)):
                seq_record.id = "Ccanephora"
            if (re.match('^ia\d{2}g', seq_record.id)):
                seq_record.id = "Iaquatica"
            if (re.match('^ib\d{2}g', seq_record.id)):
                seq_record.id = "Ibatatas"
            if (re.match('^Ica\d{2}g', seq_record.id)):
                seq_record.id = "Icairica"
            if (re.match('^in\d{2}g', seq_record.id)):
                seq_record.id = "Inil"
            if (re.match('^if\d{2}g', seq_record.id)):
                seq_record.id = "Itrifida"
            if (re.match('^il\d{2}g', seq_record.id)):
                seq_record.id = "Itriloba"
            if (re.match('^na\d{2}g', seq_record.id)):
                seq_record.id = "Nattenuata"
            if (re.match('^nt\d{2}g', seq_record.id)):
                seq_record.id = "Ntabacum"
            if (re.match('^Peinf', seq_record.id)):
                seq_record.id = "Pinflata"
            if (re.match('^Peaxi', seq_record.id)):
                seq_record.id = "Paxillaris"
            if (re.match('^sh\d{2}g', seq_record.id)):
                seq_record.id = "Schacoense"
            if (re.match('^sl\d{2}g', seq_record.id)):
                seq_record.id = "Slycopers"
            if (re.match('^sm\d{2}g', seq_record.id)):
                seq_record.id = "Smelongena"
            if (re.match('^sp\d{2}g', seq_record.id)):
                seq_record.id = "Spennellii"
            if (re.match('^st\d{2}g', seq_record.id)):
                seq_record.id = "Stuberosum"
            if (re.match('^vv\d{2}g', seq_record.id)):
                seq_record.id = "Vvinifera"
            seq_record.description = seq_record.id
            seqList.append(seq_record)
        SeqIO.write(seqList, "./singleCopySeq/"+id+"sta", "fasta")

