#!/bin/bash
#PBS -N hal2maf
#PBS -l nodes=1:ppn=6
#PBS -l mem=16gb
#PBS -q cu
#PBS -o hal2maf_output.log
#PBS -e hal2maf_error.log
#PBS -t 1-18

# Change directory to the location of your script
cd /work/ZMF/accelerated-region/20species/00.CONACC/phastCon

# Define the reference genome
REF_GENOME="Duroc"

# Read the line corresponding to the current PBS_ARRAYID
line=$(sed -n "${PBS_ARRAYID}p" ./change.txt)
read -r NC chr <<< "$line"

# Execute phastCons command using specific reference sequence from change.txt
phastCons ../maf/${NC}.maf ../4d/timetree-4d.nonconserved.mod --target-coverage 0.3 --expected-length 45 --rho 0.31 --msa-format MAF --seqname chr${chr} --most-conserved timetree-20species-Alignment-pig-chr${chr}_most-4dnonconsmod.bed > timetree-20species-Alignment-pig-chr${chr}.wig

