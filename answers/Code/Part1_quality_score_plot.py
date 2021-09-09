import gzip
import matplotlib.pyplot as plt
import numpy as np
import Bioinfo

def count_quality_score_lines(file):
    '''Counts the total quality score lines in a fastq file'''
    with gzip.open(file,'rt') as fq:
        index = 0
        for i in fq:
            index += 1
        index = int(index / 4)
    return index

def line_bp_length(file):
    '''Counts the length of the first quality score line in a fastq file'''
    fq_file = gzip.open(file,'rt')
    i = 0 
    while i < 4:
        target = fq_file.readline()
        target = target.strip()
        i += 1
    total_bp = 0 
    for x in target:
        total_bp += 1
    return total_bp

def populate_array(array,file):
    '''Modifies a numpy array and sets easch index[0] in the 2d array to be equal to the sum of all
    converted phred scores of the quality score reads'''
    with gzip.open(file,'rt') as fq:
    #     creates an index for the outer loop
        index = 0
    #     i is each line in the file 
        for i in fq:
    #         remove white space on i
            i = i.rstrip()
    #     if line is a quality score line
            if index % 4 == 3:
    #             sets an index for each qual score in a line
                innerIndex = 0
    #     For each quality score in a specific line
                for j in i:
    #     Outer index is adjusted index for each line 
                    outerIndex = int(index / 4)
                    array[(innerIndex,0)] += Bioinfo.convert_phred(j)
                    innerIndex += 1
            index += 1
                    
    return array
    
def make_graph(file,graph_name):
    '''Creates a graph of mean Quality scores'''
    total_lines = count_quality_score_lines(file)
    holder = np.zeros((line_bp_length(file), 1), dtype=float)
    populated_array = populate_array(holder,file)
    dev_x = range(len(holder))
    dev_y = np.divide(populated_array, total_lines)
    plt.xlabel('Position')
    plt.ylabel('Mean Quality Score')
    plt.title('Mean Quality Scores from Illumina Reads')
    plt.plot(dev_x,dev_y)
    plt.savefig(f'{graph_name}.png')
    plt.clf()
    plt.cla()

def main():
    # read_1_7_2E = '/projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz'
    # read_2_7_2E = '/projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz'
    read_1_19_3F= '/projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz'
    read_2_19_3F = '/projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz'
  
    # make_graph(read_1_7_2E,'read_1')
    # make_graph(read_2_7_2E,'read_02')
    make_graph(read_1_19_3F,'19_3F_fox_S14_L008_R1_001_Personal_plot.png')
    make_graph(read_2_19_3F,'19_3F_fox_S14_L008_R2_001_Personal_plot.png')
    
if __name__ == '__main__':
    main()