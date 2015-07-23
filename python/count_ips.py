from collections import Counter

def read_data(file1):
    ls1 = []
    ls2 = []
    with open(file1, 'r') as f: 
        for line in f:
            #print line
            ls1 = line.split(',')
            #ls2.append(ls1[2])
        print ls1, ls2
        c = Counter(ls2)
            # { 
        count = 0
            #for k,v in c:
            #    if v == 1:
            #       count +=1
            #    print count 

read_data('configs/amazon.txt')