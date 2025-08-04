import pandas as pd  
import numpy as np  
import argparse

parser = argparse.ArgumentParser(description='Number of random samples')
parser.add_argument('--sample_size', type=int, required=True, help='Number of random samples')
args = parser.parse_args()

#read bed file
bed_file = 'filter-timetree-allmod4dnonconsmod.bed'  
df = pd.read_csv(bed_file, sep='\t', header=None, names=['chrom', 'start', 'end'])  

#Initialize an empty list to store all median distances and cluster counts
medians = []  
cluster_counts = []

# calculate cluster funtion
def calculate_clusters(df, max_distance=50000, min_cluster_size=3):
    clusters = []
    current_cluster = []

    for index, row in df.iterrows():
        if not current_cluster:
            current_cluster.append(row)
        else:
            last_row = current_cluster[-1]
            if row['chrom'] == last_row['chrom'] and (row['start'] - last_row['end']) <= max_distance:
                current_cluster.append(row)
            else:
                if len(current_cluster) >= min_cluster_size:
                    clusters.append(current_cluster)
                current_cluster = [row]
    
    # check cluster
    if current_cluster and len(current_cluster) >= min_cluster_size:
        clusters.append(current_cluster)

    return len(clusters)

#Repeat random sampling and calculation 1000 times
for _ in range(1000):  
    indices = np.random.choice(df.index, args.sample_size, replace=False)  
    sample_df = df.loc[indices].reset_index(drop=True)  
    
    #Sort the sampled data
    sample_df = sample_df.sort_values(by=['chrom', 'start']).reset_index(drop=True)

    # Calculate the number of clusters in the current sample
    num_clusters = calculate_clusters(sample_df)

    #Save the cluster count
    cluster_counts.append(num_clusters)

    #Initialize an empty list to store distances
    distances = []  
    
    #Iterate through each row and calculate the distance to the next row
    for index, row in sample_df.iterrows():  
        if index + 1 < len(sample_df): 
            chrom1, start1, end1 = row  
            chrom2, start2, end2 = sample_df.loc[index + 1]  
              
            #Skip if the two rows belong to different chromosomes
            if chrom1 != chrom2:  
                continue  
              
            #Calculate the distance between the end of the current interval and the start of the next interval
            distance = start2 - end1  
            distances.append(distance)  
    
    #Calculate the median of the distances
    if distances:  
        median_distance = np.median(distances)  
        medians.append(median_distance)  

median_df = pd.DataFrame(medians, columns=['Median_Distance'])  
cluster_df = pd.DataFrame(cluster_counts, columns=['Cluster_Count'])  

#combined
result_df = pd.concat([median_df, cluster_df], axis=1)


result_df.to_csv('{}Median_Distances_and_Cluster_Counts.csv'.format(args.sample_size), sep=',', index=False, header=True)  

print("Calculation completed; median distances and cluster counts have been saved to'{}Median_Distances_and_Cluster_Counts.csv'".format(args.sample_size))
