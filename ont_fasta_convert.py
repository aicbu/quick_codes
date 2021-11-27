#!/usr/bin/env python
# coding: utf-8

from Bio import SeqIO
#import sys
#import os

ont_run='5'
barcodes=[]
seqs=[]
new_name = 'hCoV-19/SriLanka/aicbu'
year = '2021'
new_file="ont_"+ont_run+"_names_replaced.fasta"

multi_fasta = SeqIO.parse(open('ont_5_consensus.fasta'), 'fasta')
for record in multi_fasta:
    seqs.append(record.seq)
    seq_id=record.id.split("barcode")[1]
    barcodes.append(seq_id)

len(barcodes)

with open(new_file,'w') as output:
    for n in range(len(barcodes)):
        output.write('>'+ new_name + ont_run + str(barcodes[n])+'/'+year+'\n')
        output.write(str(seqs[n])+'\n')






