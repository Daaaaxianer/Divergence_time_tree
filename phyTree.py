# -*- coding:utf-8 -*-
# @FileName :phyTree.py
# @Time     :2023/1/2 23:41
# @Author   :Xian

import re
from Bio import AlignIO
import argparse

def cleanTree(intree,outtree):
    '''Clean nodes and labels in the tree file'''
    with open(intree,'r') as intr:
        trees = intr.read()
        replaceTree = re.sub(r"[:\d+\.\d+]","",trees)
        print(replaceTree)
    with open(outtree, 'w') as outtr:
        outtr.write(replaceTree)
def converttree(intree,formatin,outtree,formatout):
    '''Convert tree format'''
    AlignIO.convert(intree,formatin,outtree,formatout)

def nwkTimeMultiply(intree,outtree):
    '''The time of the ultrametric tree multiplied by 100'''
    with open(intree,'r') as intr:
        treein = intr.read()
        arra = re.split(r',',treein)
        arrb = []
        for tra in arra:
            print (f"a split : {tra}")
            trb = re.split(r':',tra)
            # print (f"b split : {trb}")
            trb[-1] = str(float(trb[-1]) * 100)
            # print(f"b split 1 : {trb[1]}")
            arrb.append(":".join(trb))
        treeout = ",".join(arrb)
    with open(outtree, 'w') as outtr:
        outtr.write(treeout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="用途：操作进化树")
    parser.add_argument("-ci","--cleantree", action="store_true", help="Clear the branches and node of nwick tree")
    parser.add_argument("-cl","--converttree", action="store_true", help="Convert the format of the tree(Support: Newick, NEXUS, phyloXML and NeXML)")
    parser.add_argument("-tm","--timemutiply", action="store_true", help="The time of the ultrametric tree(Newick) multiplied by 100)")
    parser.add_argument("-it","--intree", type=str,help="input tree file  (type = str)")
    parser.add_argument("-ot","--outtree", type=str, help="output tree file  (type = str)")
    parser.add_argument("-if", "--formatin", type=str, help="format of input tree file (type = str)")
    parser.add_argument("-of", "--formatout", type=str, help="format of output tree file (type = str)")

    args = parser.parse_args()

    if args.cleantree:
        cleanTree(args.intree,args.outtree)
    if args.converttree:
        converttree(args.intree,args.formatin,args.outtree,args.formatout)
    if args.timemutiply:
        nwkTimeMultiply(args.intree,args.outtree)
