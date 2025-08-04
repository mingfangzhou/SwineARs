from Bio import AlignIO

# species number
total_species = 20
required_species = {
    "Duroc", "Norwegian_Landrace", "Pietrain", 
    "Large_White", "Chenghua", "Ningxiang", 
    "Meishan", "Bama"
}

# 
specific_species = {
    "Catagonus_wagneri", "Bos_taurus", "Ovis_aries", 
    "Homo_sapiens", "Felis_catus", "Canis_lupus", 
    "Oryctolagus_cuniculus", "Mus_musculus"
}

try:
    alignment = AlignIO.parse("20species-mask-Alignment-rmDupes-Orthologs.maf", "maf")
except Exception as e:
    print(f"Error reading MAF file: {e}")
    exit()

try:
    with open("Final-20species-filter-block_alignment-keep8_out2.maf", "w") as output_handle:
        for block in alignment:
            species_set = {record.id.split('.')[0] for record in block}
            num_present_required_species = sum(1 for species in required_species if species in species_set)
            num_present_specific_species = sum(1 for species in specific_species if species in species_set)

            # ensure  exits at least two specific_species
            if (required_species.issubset(species_set) and num_present_specific_species >= 2):
                AlignIO.write([block], output_handle, "maf")  
except Exception as e:
    print(f"Error writing MAF file: {e}")

