import pandas as pd
import numpy as np

data = pd.read_csv("physics_data.csv",index_col=0)
inst_dict = {0:"Haifa", 1:"OpenU", 2:"BIU", 3:"TAU", 4:"Ariel", 5:"Technion", 6:"BGU",
        7:"HUJI", 8:"WIS", 9:"USA", 10:"Europe", 11:"USSR"}
edges = []

# generate all permutations with itertools and then access data using keys and institute_dictionary
for i,j in enumerate(data):
    for k,l in enumerate(data):
        if data[l][i] > 0:
            edges.append((i,k,data[l][i]))
    #for j in data[i]:
     #   print(j)
#print(data)
print(edges)
#print(data.index.values)


# add some asserts
assert len(edges) == np.count_nonzero(data)
