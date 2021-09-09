#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --time=5:00:00
conda activate bgmp_py39

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
 --outFilterMultimapNmax 3 \
 --outSAMunmapped Within KeepPairs \
 --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
 --readFilesCommand zcat \
 --readFilesIn /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/adapter_work/7_2E_fox__R1_trimmed_adptrmv.fq.gz  /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/adapter_work/7_2E_fox__R2_trimmed_adptrmv.fq.gz \
 --genomeDir /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/Mouse.GRCm39.dna.ens104.STAR_2.7.9a \
 --outFileNamePrefix Mouse

 echo 'done'

 exit