#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --time=2:00:00

conda activate bgmp_py39

/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate \
--genomeDir /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/Mouse.GRCm39.dna.ens104.STAR_2.7.9a \
--genomeFastaFiles /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/Mus_musculus.GRCm39.dna.primary_assembly.fa \
--sjdbGTFfile /projects/bgmp/tcollin2/bioinfo/Bi623/PS/QAA_Work/genome/Mus_musculus.GRCm39.104.gtf


 exit