# Alex Tuttle's Homework #4

#1.0 load in data file for read
# 1.1.1- import libraries and dataset
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.75)
import pandas as pd
#1.1.2- reading in data and making graph
with open("viral_data.csv", "r") as data:
    dataframe = pd.read_csv("viral_data.csv", header = 0)
 #matplotlib violin plot
    sns.set(font_scale = 2)
    with sns.color_palette("Blues"):
         sns.set_style("whitegrid")
         vlnplot = sns.violinplot(x= 'protein_structure', y='gene_expression_level', data=dataframe)
#adding title
    vlnplot.set (xlabel='', ylabel= 'Expression Level', title = 'Virus X Gene Expression Levels', ylim = (-100,800))
    
    #print(vlnplot)
    plt.savefig("viral_gene_expression.png")

#%%
#1.1.3- identifying top genes in csv file by viral gene expression
with open("viral_data.csv", "r") as data:
    df = pd.read_csv("viral_data.csv", header = 0) #loading .tsv file into pandas for data read
    df_sort = df.sort_values(["gene_expression_level"], ascending = False) #sorting viruses by gene expression level
    #print(df_sort)
    target_candidates= df_sort.iloc[:2, 3]
    print(target_candidates) #overall top 2 candidates
    
#%%
#1.1.4 Top 2 genes both by protein structural and nonstructural categories
with open("viral_data.csv", "r") as data:
    df = pd.read_csv("viral_data.csv", header = 0) #loading .tsv file into pandas for data read
    df_sort1 = df.sort_values(["protein_structure", "gene_expression_level"], ascending = [False, False])
    df_sort2 = df.sort_values(["protein_structure", "gene_expression_level"], ascending = [True, False])
    target_candidates_struct= df_sort1.iloc[:2, 3]
    target_candidates_non = df_sort2.iloc[:2, 3]
    print(target_candidates_struct,target_candidates_non)
    

    
  
    
    


#%%
#1.2 scatterplot- first step, load dataframe
with open("phase1.tsv", "r") as data:
    dataframe = pd.read_csv("phase1.tsv", sep= "\t", header = 0)
    #print(dataframe)
    sns.set(font_scale = 2)
    with sns.color_palette("dark"):
        sns.set_style("whitegrid")# changing to a white backgroung
        lnplt = sns.lmplot(x = "# Treated", y="# Cured", data=dataframe) #defining new graph for manipulation
        lnplt.set(xlabel = "Patients Treated", ylabel= "Pateients Cured", title = "Phase I Drug Trials") #adding axes, graph title
        #print(lnplt)
        plt.savefig("Phase1.png")
        

