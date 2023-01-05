# -*- coding:utf-8 -*-
# @FileName :deleteStopCodon.py
# @Time     :2022/2/10 11:49
# @Author   :Xian

## 脚本使用顺序 filterSingleCopySequence.py --> batchFileRename.py --> batchFile2Phy.py --> phylipConvert.py -->deleteStopCodon.py
import re

with open(r'all.phys', 'r') as f:
    content = f.read()
    content = content.replace("TAG","---")
    content = content.replace("TAA", "---")
    content = content.replace("TGA", "---")
    # print(content)

with open('all.delStopCodon.phys', 'w') as f:
    f.write(content)