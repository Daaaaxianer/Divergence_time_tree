# -*- coding:utf-8 -*-
# @FileName :phylipConvert.py
# @Time     :2022/2/10 10:47
# @Author   :Xian

### 将多序列比对的fasta格式转换为 phylip Sequential格式(与muscle的-physout输出格式并不一致)
## 脚本使用顺序 filterSingleCopySequence.py --> batchFileRename.py --> batchFile2Phy.py --> phylipConvert.py -->deleteStopCodon.py

import re
from paml_mcmctree.batchFile2Phy import getFile

def fas2phy(infas):
    with open(infas, 'r') as fin:
        sequences = [(m.group(1), ''.join(m.group(2).split()))
                     for m in re.finditer(r'(?m)^>([^ \n]+)[^\n]*([^>]*)', fin.read())]
        with open(infas+".phy", 'w') as fout:
            fout.write('%d %d\n' % (len(sequences), len(sequences[0][1])))
            for item in sequences:
                fout.write('%-20s %s\n' % item)

if __name__ == '__main__':
    name = getFile("./singleCopySeq", ".fas")
    for id in name:
        print ("Conerting "+id )
        fas2phy("./singleCopySeq/"+id)