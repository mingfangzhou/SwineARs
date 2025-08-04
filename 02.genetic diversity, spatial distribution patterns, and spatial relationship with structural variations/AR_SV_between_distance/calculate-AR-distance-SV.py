import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description='Calculate the distance from each AR to its nearest SV')
parser.add_argument('--input_file', type=str, required=True, help='input bed file')
parser.add_argument('--sv_file', type=str, required=True, help='input SV position file')
args = parser.parse_args()

##check file exit##
if not os.path.exists(args.input_file):
    raise FileNotFoundError(f"file {args.input_file} no")
if not os.path.exists(args.sv_file):
    raise FileNotFoundError(f"file{args.sv_file} no")

# read bed file
df = pd.read_csv(args.input_file, sep='\t', header=None, names=['chrom', 'start', 'end'])

#Read SV file (containing only chromosome and start position)
sv_df = pd.read_csv(args.sv_file, sep='\t', header=None, names=['chrom', 'sv_start'])

#Check file format
if df.shape[1] != 3:
    raise ValueError(f"文件 {args.input_file} format incorrect, should contain 3 columns")
if sv_df.shape[1] != 2:
    raise ValueError(f"文件 {args.sv_file} format incorrect, should contain 2 columns")

#Create an empty list to store results
results = []

#Iterate through each row and calculate the distance to the nearest SV
for i in range(len(df)):
    chrom1, start1, end1 = df.loc[i]
    
    #Get all SVs on the same chromosome as the current region
    sv_chrom_df = sv_df[sv_df['chrom'] == chrom1]
    
    #Calculate distances from the current region to each SV
    distances = []
    for _, sv_row in sv_chrom_df.iterrows():
        sv_start = sv_row['sv_start']
        
        #Calculate the minimal distance between the region and the SV
        if end1 < sv_start:
            distance = sv_start - end1  #SV is after the region
        elif start1 > sv_start:
            distance = start1 - sv_start  #SV is before the region
        else:
            distance = 0  #Region overlaps with SV, distance is 0
            
        distances.append(distance)
    
    #Find the minimum distance to the nearest SV
    min_distance = min(distances) if distances else None
    if min_distance is not None:
        results.append([chrom1, start1, end1, min_distance])

#Convert results to a DataFrame
result_df = pd.DataFrame(results, columns=['chrom', 'start', 'end', 'nearest_sv_distance'])


base_name = os.path.splitext(args.input_file)[0]
output_file = f'{base_name}_test-AR_and_SV_distances.bed'
median_file = f'{base_name}_test-median_SV_distance.txt'

#Save the results to a new file
result_df.to_csv(output_file, sep='\t', index=False, header=True)

#Calculate the median distance
median_distance = result_df['nearest_sv_distance'].median()

#Save the median distance to the specified file
with open(median_file, 'w') as f:
    f.write(f'Median_Distance: {median_distance}\n')

print(f"Calculation completed. Results saved to '{output_file}', median saved to '{median_file}'")

