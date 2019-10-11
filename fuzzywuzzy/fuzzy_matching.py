from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

data1=pd.read_table("drugsComTrain_raw.tsv",sep='\t')
data2=pd.read_table("drugsComTest_raw.tsv",sep='\t')
data3=pd.read_table("drugLibTrain_raw.tsv",sep='\t')
data4=pd.read_table("drugLibTest_raw.tsv",sep='\t')
data5=pd.read_table("drugs.tsv",sep='\t')
data6=pd.read_table("indications.tsv",sep='\t')

drugs_names=[]
# for i in range(len(data1)):
#     drugs_names.append(data1.loc[i,"drugName"])
# for i in range(len(data2)):
#     drugs_names.append(data2.loc[i,"drugName"])
# for i in range(len(data3)):
#     drugs_names.append(data3.loc[i,"urlDrugName"])
# for i in range(len(data4)):
#     drugs_names.append(data4.loc[i,"urlDrugName"])
for i in range(len(data5)):
    drugs_names.append(data5.loc[i,"drug"])
# for i in range(len(data6)):
#     drugs_names.append(data6.loc[i,"drug"])


def find_Drug_Name(word):
    max_score=0.0
    output_drug=""
    for i in range(len(drugs_names)):
        curr_score=fuzz.token_set_ratio(word,drugs_names[i])
        if(curr_score > max_score):
            max_score=curr_score
            output_drug=drugs_names[i]

    output=[output_drug,max_score]
    return output