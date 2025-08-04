#!/bin/bash
#PBS -N phylop
#PBS -l nodes=1:ppn=1
#PBS -l mem=10gb
#PBS -q cu
#PBS -o /home/zhoumingfang/log/phylop_output.log
#PBS -e /home/zhoumingfang/log/phylop_error.log
#PBS -t 1-18

# Change directory to the location of your script

cd /work/ZMF/accelerated-region/20species/00.CONACC/phylop

# Define the reference genome
REF_GENOME="Pig"

# Read the line corresponding to the current PBS_ARRAYID
line=$(sed -n "${PBS_ARRAYID}p" ../change.txt)
read -r NC chr <<< "$line"

phyloP --branch Asia --msa-format MAF --features ../phastCon/timetree-chr${chr}mod4dnonconsmod.bed --method LRT --mode CONACC  ../4d/named_timetree-4d.nonconserved.mod  ../maf/${NC}.maf  > timetree-CONACC-20species.4d-branch-Asia-chr${chr}.bed



phyloP --branch Europe --msa-format MAF --features ../phastCon/timetree-chr${chr}mod4dnonconsmod.bed --method LRT --mode CONACC ../4d/named_timetree-4d.nonconserved.mod ../maf/${NC}.maf > timetree-CONACC-20species.4d-branch-Europe-chr${chr}.bed

phyloP --branch Anc --msa-format MAF --features ../phastCon/timetree-chr${chr}mod4dnonconsmod.bed --method LRT --mode CONACC ../4d/named_timetree-4d.nonconserved.mod ../maf/${NC}.maf > timetree-CONACC-20species.4d-branch-Anc-chr${chr}.bed






