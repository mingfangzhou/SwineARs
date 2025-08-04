#!/bin/bash

mkdir -p chr_gff_files


while read -r ref chr; do

  awk -v ref="$ref" '$2 == ref {
    $2 = "";  
    print $1, $3, $4, $5, $6, $7, $8, $9;  
  }' OFS="\t" genes.gff > "chr_gff_files/${chr}.gff"

  MAF_PATH="../maf/${ref}.maf"

  # 4d site
  msa_view $MAF_PATH --in-format MAF --4d --features "chr_gff_files/${chr}.gff" > "${chr}.4d-codons.ss"
  # 
  msa_view "${chr}.4d-codons.ss" --in-format SS --out-format SS --tuple-size 1 > "${chr}.4d-sites.ss"
done < ./change.txt

