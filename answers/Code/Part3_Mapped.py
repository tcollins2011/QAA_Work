# Mapped Reads: 10928151
# Unmapped Reads: 820328

import re

# Determines count of mapped and unmapped reads from sam file
def main(file):
    mapped:int = 0
    unmapped:int = 0
    non_dup:dict = {}
    
    # Loop though file and remove headers. Place 1 of each paired end read in a dict
    with open(file,'r') as fh:
        for line in fh: 
            if line[0] != '@':
                line = line.strip()
                split_line = re.split('\t',line)
                mapid = split_line[0]
                if mapid not in non_dup.keys(): 
                    non_dup[mapid] = split_line[1]
    
    # Checks to see if each unique read is mapped or unmapped and tallies them
    for value in non_dup.values():
        if((int(value) & 4) != 4):
            mapped +=1
        else:
            unmapped += 1
    print(mapped)
    print(unmapped)

                
if __name__=='__main__':
    main('./Aligned/Danio_rerioAligned.out.sam')