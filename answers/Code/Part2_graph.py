# This script will create a graph of mean read length distribution
import gzip
import matplotlib.pyplot as plt
import sys

def make_graph(read1,read2,read1Name,read2Name):
    '''Creates a graph of quality score counts'''
    lists1 = sorted(read1.items()) 
    x1, y1 = zip(*lists1) 

    lists2 = sorted(read2.items()) 
    x2, y2 = zip(*lists2) 

    plt.xlabel('Length')
    plt.ylabel('Percent Frequency')
    plt.title('Percentage of reads at each length')

    plt.plot(x1, y1, label='read1')
    plt.plot(x2, y2, label='read2')
    plt.legend()
    plt.savefig(f'{read1Name} vs {read2Name} Length Distribution.png')

def get_file_counts(file):
    '''Returns a dictionary that contains the percent of total reads at each length in the file'''
    counter_dict = dict()
    for i in range(102):
        counter_dict[i] = 0
    
    with gzip.open(file,'rt') as fq:
        line_count = 0
        for line in fq:
            line_count += 1
            if line_count % 4 == 2:
                target = line.strip()
                length = 0
                for x in target:
                    length += 1
                if length in counter_dict:
                    counter_dict[length] += 1
    counter_dict = {k: v / total for total in (sum(counter_dict.values()),) for k, v in counter_dict.items()}
    return counter_dict

def main():
    read1 = sys.argv[1]
    read2 = sys.argv[2]
    
    read_1_count = get_file_counts(read1)
    read_2_count = get_file_counts(read2)
    
    make_graph(read_1_count, read_2_count, read1, read2)
    
if __name__ == '__main__':
    main()