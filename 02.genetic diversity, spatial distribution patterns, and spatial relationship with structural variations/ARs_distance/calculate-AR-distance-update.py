import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description='calculate AR distance')
parser.add_argument('--input_file', type=str, required=True, help=' input bed file')
args = parser.parse_args()

#read bed file
df = pd.read_csv(args.input_file, sep='\t', header=None, names=['chrom', 'start', 'end'])

results = []

#Iterate through each row and calculate the distance to the next row
for i in range(len(df) - 1):
    chrom1, start1, end1 = df.loc[i]
    chrom2, start2, end2 = df.loc[i + 1]
    
    # Skip if the two rows belong to different chromosomes
    if chrom1 != chrom2:
        continue
    
    #Calculate the distance between the end of the current interval and the start of the next interval
    distance = start2 - end1
    results.append([chrom1, start1, end1, chrom2, start2, end2, distance])

result_df = pd.DataFrame(results, columns=['chrom1', 'start1', 'end1', 'chrom2', 'start2', 'end2', 'distance'])

base_name = os.path.splitext(args.input_file)[0]
output_file = f'{base_name}_AR_distances.bed'
median_file = f'{base_name}_median_distance.txt'

#outfile
result_df.to_csv(output_file, sep='\t', index=False, header=False)

#Compute the median distance
median_distance = result_df['distance'].median()


with open(median_file, 'w') as f:
    f.write(f'Median_Distance: {median_distance}\n')

print(f"end calculate")
