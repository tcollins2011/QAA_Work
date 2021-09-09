#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8

conda activate bgmp_py39

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
 --outFilterMultimapNmax 3 \
 --outSAMunmapped Within KeepPairs \
 --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
 --readFilesCommand zcat \
 --readFilesIn /projects/bgmp/shared/Bi621/dre_WT_ovar12_R1.qtrim.fq.gz /projects/bgmp/shared/Bi621/dre_WT_ovar12_R2.qtrim.fq.gz \
 --genomeDir /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/Mouse.GRCm39.dna.ens104.STAR_2.7.9a \
 --outFileNamePrefix Mouse

 echo 'done'

 exit