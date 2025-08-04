msa_view --unordered-ss --out-format SS --aggregate  Duroc,Babyrousa_celebensis,Bama,Bos_taurus,Canis_lupus,Catagonus_wagneri,Chenghua,Felis_catus,Meishan,Mus_musculus,Norwegian_Landrace,Oryctolagus_cuniculus,Ovis_aries,Sus_cebifrons,Homo_sapiens,Large_White,Phacochoerus_africanus,Pietrain,Potamochoerus_porcus,Ningxiang  chr1.4d-sites.ss,chr2.4d-sites.ss,chr3.4d-sites.ss,chr4.4d-sites.ss,chr5.4d-sites.ss,chr6.4d-sites.ss,chr7.4d-sites.ss,chr8.4d-sites.ss,chr9.4d-sites.ss,chr10.4d-sites.ss,chr11.4d-sites.ss,chr12.4d-sites.ss,chr13.4d-sites.ss,chr14.4d-sites.ss,chr15.4d-sites.ss,chr16.4d-sites.ss,chr17.4d-sites.ss,chr18.4d-sites.ss > all-4d.sites.ss

phyloFit --tree ./20species-timetree.nwk  -i SS all-4d.sites.ss --out-root timetree-4d.nonconserved

