
##########Asia lineage###########
asia_data <- read.table("positiveACC-20species_Asia_regions_gc_content.txt", header = FALSE, sep = " ")

colnames(asia_data) <- c("chr", "start", "end", "name", "null_scale", "alt_scale", "alt_subscale", "lnlratio", "pval",
                         "pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T", "num_N", "num_oth", "seq_len")

# calculate adjust p value
asia_data$adjusted_P_value <- p.adjust(asia_data$pval, method = "BH")

asia_data$length <- asia_data$end - asia_data$start 


significant_asia <- asia_data[asia_data$adjusted_P_value < 0.05, ]

write.table(significant_asia, "significant_asia.txt", quote = FALSE, row.names = FALSE, col.names = FALSE,sep = "\t")



##read gbGC region data
significant_filterBia_Asia <- read.table("significant_filterBia_Asia.txt", header = F, sep = "\t")


colnames(significant_filterBia_Asia) <- c("chr", "start", "end", "name", "null_scale","alt_scale" ,"alt_subscale" ,"lnlratio", "pval","pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T",
                                            "num_N", "num_oth", "seq_len","adjusted_P_value","length")



# alt_subscale  log10 change
significant_filterBia_Asia$log_alt_subscale <- log10(significant_filterBia_Asia$alt_subscale)

selected_Asia_columns <- significant_filterBia_Asia[, c("chr", "start", "end","log_alt_subscale")]

write.table(selected_Asia_columns, "Asia-significant-accelerated-region.txt", quote = FALSE, row.names = FALSE, col.names = TRUE, sep="\t")



##########Europe lineage############

Europe_data <- read.table("positiveACC-20species_Europe_regions_gc_content.txt", header = FALSE, sep = " ")


colnames(Europe_data) <- c("chr", "start", "end", "name", "null_scale", "alt_scale", "alt_subscale", "lnlratio", "pval",
                         "pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T", "num_N", "num_oth", "seq_len")


Europe_data$adjusted_P_value <- p.adjust(Europe_data$pval, method = "BH")


Europe_data$length <- Europe_data$end - Europe_data$start 


significant_Europe <- Europe_data[Europe_data$adjusted_P_value < 0.05, ]


write.table(significant_Europe, "significant_Europe.txt", quote = FALSE, row.names = FALSE, col.names = FALSE, sep = "\t")


significant_filterBia_Europe <- read.table("significant_filterBia_Europe.txt", header = F, sep = "\t")


colnames(significant_filterBia_Europe) <- c("chr", "start", "end", "name", "null_scale","alt_scale" ,"alt_subscale" ,"lnlratio", "pval","pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T",
                                          "num_N", "num_oth", "seq_len","adjusted_P_value","length")


significant_filterBia_Europe$log_alt_subscale <- log10(significant_filterBia_Europe$alt_subscale)


selected_Europe_columns <- significant_filterBia_Europe[, c("chr", "start", "end","log_alt_subscale")]


write.table(selected_Europe_columns, "Europe-significant-accelerated-region.txt", quote = FALSE, row.names = FALSE, col.names = TRUE, sep="\t")



##########Ancestor lineage########

Anc_data <- read.table("positiveACC-20species_Anc_regions_gc_content.txt", header = FALSE, sep = " ")


colnames(Anc_data) <- c("chr", "start", "end", "name", "null_scale", "alt_scale", "alt_subscale", "lnlratio", "pval",
                           "pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T", "num_N", "num_oth", "seq_len")


Anc_data$adjusted_P_value <- p.adjust(Anc_data$pval, method = "BH")


Anc_data$length <- Anc_data$end - Anc_data$start 

significant_Anc <- Anc_data[Anc_data$adjusted_P_value < 0.05, ]

write.table(significant_Anc, "significant_Anc.txt", quote = FALSE, row.names = FALSE, col.names = FALSE, sep = "\t")


significant_filterBia_Anc <- read.table("significant_filterBia_Anc.txt", header = F, sep = "\t")


colnames(significant_filterBia_Anc) <- c("chr", "start", "end", "name", "null_scale","alt_scale" ,"alt_subscale" ,"lnlratio", "pval","pct_at", "pct_gc", "num_A", "num_C", "num_G", "num_T",
                                            "num_N", "num_oth", "seq_len","adjusted_P_value","length")


sum_length_Anc_rmBia <- sum(significant_filterBia_Anc$length)


significant_filterBia_Anc$log_alt_subscale <- log10(significant_filterBia_Anc$alt_subscale)

selected_Anc_columns <- significant_filterBia_Anc[, c("chr", "start", "end","log_alt_subscale")]


write.table(selected_Anc_columns, "Anc-significant-accelerated-region.txt", quote = FALSE, row.names = FALSE, col.names = TRUE, sep="\t")

