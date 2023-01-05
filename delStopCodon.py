# -*- coding:utf-8 -*-
# @FileName :delStopCodon.py
# @Time     :2022/2/10 11:49
# @Author   :Xian

## Delete the stop codon in the sequence
## 删除序列中的终止密码子
## 脚本使用顺序 extractSingleCopySequence.py --> batchId2Spname.py --> batchSeqAlign.py --> fasAlign2phy.py -->delStopCodon.py

import re
import argparse

def delStopCodon(inphy,outphy):
    with open(inphy,'r') as fin:
        content = fin.read()
        content = content.replace("TAG","---")
        content = content.replace("TAA", "---")
        content = content.replace("TGA", "---")
    with open(outphy,'w') as fout:
        fout.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "用途：删除比对序列中的终止密码子。")
    parser.add_argument("inalign", type = str, help = "Input file for sequence alignment (type = str)") 
    parser.add_argument("outalign", type = str, help = "Output file for sequence alignment (type = str)") 
    args = parser.parse_args()
    
    delStopCodon(args.inalign,args.outalign)
