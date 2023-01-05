# -*- coding:utf-8 -*-
# @FileName :transAlign.py
# @Time     :2023/1/3 1:30
# @Author   :Xian

from Bio import AlignIO

# alignments = AlignIO.parse("resampled.phy", "phylip-sequential")

AlignIO.convert("OG0012653.singlecopy.cds.fasta.fas", "fasta", "OG0012653.singlecopy.cds.fasta.fas.phy", "phylip-relaxed")