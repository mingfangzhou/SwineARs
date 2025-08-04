import pandas as pd
import numpy as np
import argparse
import os

#Parse command-line arguments
parser = argparse.ArgumentParser(description='Randomly sample intervals and calculate the distance to the nearest SV, then compute the median')
parser.add_argument('--sample_size', type=int, required=True, help='Number of intervals to sample each time')
parser.add_argument('--sv_file', type=str, required=True, help='SV position file')
args = parser.parse_args()

#Check if the input SV file exists
if not os.path.exists(args.sv_file):
    raise FileNotFoundError(f"File {args.sv_file} does not exist")

#Read the BED file
bed_file = 'chrfilter-timetree-allmod4dnonconsmod.bed'  
df = pd.read_csv(bed_file, sep='\t', header=None, names=['chrom', 'start', 'end'])  

#Read the SV file (only chromosome and start position)
sv_df = pd.read_csv(args.sv_file, sep='\t', header=None, names=['chrom', 'sv_start'])

#Group SV data by chromosome and create a dictionary for faster lookup
sv_dict = sv_df.groupby('chrom')['sv_start'].apply(list).to_dict()

#Initialize an empty list to save median distances from each calculation
medians = []

#Calculate the nearest SV distance for sampled intervals
def calculate_nearest_sv_distance(sample_df, sv_dict):
    min_distances = []  #Store the minimum distance to the nearest SV for each interval
    
    for _, row in sample_df.iterrows():
        chrom1, start1, end1 = row['chrom'], row['start'], row['end']
        
        # Get all SVs on the same chromosome as the current interval
        sv_chrom_list = sv_dict.get(chrom1, [])
        
        if not sv_chrom_list:
            continue  #Skip if no SVs on this chromosome
        
        #Calculate distances from the interval to all SVs on the chromosome
        distances = []  
        for sv_start in sv_chrom_list:
            #Calculate distance between the interval and the SV
            if end1 < sv_start:
                distance = sv_start - end1  #SV is after the interval
            elif start1 > sv_start:
                distance = start1 - sv_start  #SV is before the interval
            else:
                distance = 0  #Interval overlaps SV, distance is 0
            
            distances.append(distance)
        
        #Choose the minimum distance to the nearest SV
        min_distance = min(distances) if distances else None
        if min_distance is not None:
            min_distances.append(min_distance)
    
    #Return the median of the minimum distances
    return np.median(min_distances) if min_distances else None

#Repeat random sampling and distance calculation 1000 times
for _ in range(1000):
    #Repeat random sampling and distance calculation 1000 times
    indices = np.random.choice(df.index, args.sample_size, replace=False)
    sample_df = df.loc[indices].reset_index(drop=True)
    
    #Calculate the median distance for this sample
    median_distance = calculate_nearest_sv_distance(sample_df, sv_dict)
    
    if median_distance is not None:
        medians.append(median_distance)

#Convert the results into a DataFrame
median_df = pd.DataFrame(medians, columns=['Median_Distance'])

# Save the results to a new CSV file
result_file = f'{args.sample_size}_Median_test-SV_Distances.csv'
median_df.to_csv(result_file, sep=',', index=False, header=True)

print(f"Calculation completed. Median distances saved to '{result_file}'")

