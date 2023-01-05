# -*- coding:utf-8 -*-
# @FileName :phyTree.py
# @Time     :2023/1/2 23:41
# @Author   :Xian

import re
import argparse

def cleanTree(intree,outtree):
    '''Clean nodes and labels in the tree file'''
    with open(intree,'r') as intr:
        trees = intr.read()
        replaceTree = re.sub(r"[:\d+\.\d+]","",trees)
        print(replaceTree)
    with open(outtree, 'w') as outtr:
        outtr.write(replaceTree)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="用途：操作进化树")
    parser.add_argument("intree", type=str,help="input tree file in nwick formate (type = str)")
    parser.add_argument("outtree", type=str, help="output tree file in nwick formate (type = str)")
    args = parser.parse_args()
    cleanTree(args.intree,args.outtree)
