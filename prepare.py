import pandas as pd
import numpy as numpy

with open('test.txt', 'r') as f:
    target_list = [e.strip().lower() for e in f.readlines()]

df = pd.read_csv('classes_in_imagenet.csv')
df["class_name"] = df["class_name"].str.lower()


exist = []
no_exist = []

from tqdm import tqdm

for e in target_list:
    flag = True
    
    for index, row in tqdm(df.iterrows()):
        v = str(row['class_name'])
        if v == 'nan':
            continue
        if e in row['class_name']:
            exist.append(row['synid'])
            flag = False
            break
    if flag:
        no_exist.append(e)

def save_file(data, filename, sep='\n'):
    with open(filename, 'w+') as f:
        for e in data:
            f.write(e+sep)

save_file(exist, 'exist.txt', ' ')
save_file(no_exist, 'no_exist.txt', '\n')