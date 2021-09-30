#!/usr/bin/env python

import shutil, os
import argparse

parser = argparse.ArgumentParser(description="Copy ONT fastqs from each barcode")
parser.add_argument('-s', default=False, help="Source location of barcodes", required=True) 
parser.add_argument('-d', default="New_run", help="Destination location") 
parser.add_argument('-n', default=False, type=int, help="Number of Fastq files", required=True) 
args = parser.parse_args()

src=args.s
des=args.d
n=args.n

files=os.listdir(src)

print("..Creating directory New_run/")

print("No of barcodes in source: "+ str(len(files)))
print("Copying " +str(n) + " fastqs from each barcode to destination..")


#working_loop
for f in files:
    os.makedirs(os.path.join(des,f), exist_ok=True)
    print("Creating file " +f+ " and copying " +str(n)+ " fastq files..")
    jobs=0
    for fastq in os.listdir(os.path.join(src,f)):
        if jobs < n:
            shutil.copy(os.path.join(src,f,fastq),os.path.join(des,f,fastq))
            jobs+=1
print ("\nSuccessfully copied " +str(n)+ " fastq files from each " +str(len(files))+ " barcodes.")






