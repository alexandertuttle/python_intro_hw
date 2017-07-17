# Alex Tuttle's Homework #4

#1.0 load in data file for read
# 1.1.1- import libraries and dataset
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.75)
import pandas as pd

with open("viral_data.csv", "r") as data:
    dataframe = pd.read_csv("viral_data.csv", header = 0)
 #matplotlib violin plot
    vlnplot = sns.violinplot(x= 'protein_structure', y='gene_expression_level', data=dataframe)
    #plt.show()
#adding title
    vlnplot.set (xlabel='', ylabel= 'Expression Level', title = 'Virus X Gene Expression Levels', ylim = (-100,800))
    print(vlnplot)

    
    

