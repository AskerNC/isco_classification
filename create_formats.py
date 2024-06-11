import pandas as pd
import re

############## isco 08 ####################
## Load txt file into lines

import textract 

text = textract.process('structure08.docx').decode('utf-8')

lines = text.split('\n')
len(lines)

lines

def create_dataset(lines):
    isco_list = []
    name_list = []
    for line in lines:

        # Remove any inital spacing or tabs (\t)
        line = line.lstrip('\t')

        if '\t' in line:
            x = line.partition('\t')

            # Strip removes leading and traling spaces and linebreaks (\n)
            # Replace And with and, because it is not consistent
            isco_list.append(x[0].strip())
            name_list.append(x[2].strip().replace('And','and')) 

    df = pd.DataFrame({'isco08': isco_list, 'isco08_name': name_list})
    return df

df = create_dataset(lines)
df 

# Drop duplicatesd
I = df.duplicated()

df = df[~I].copy()


df['digits_level'] = df.isco08.str.len()

look = df[df.digits_level==1]

look = df[df.digits_level==2]

look = df[df.digits_level==3]

look = df[df.digits_level==4]

I = df.duplicated(subset='isco08',keep=False)
look = df[I]
# The remaing duplicates are cosmetic (weird large letters and an suffix s)

I = df.duplicated(subset='isco08',keep='first')
df = df[~I].copy()

df.to_csv('isco08_format_en.csv',index=False)
df

# Read as object to preserve leading zeros
csv = pd.read_csv('isco08_format_en.csv',dtype='object')




#### Create isco88 format

format_func  = lambda x : x.strip().lower().capitalize()

with open('isco88.txt') as f:
    lines88 = f.readlines()

lines88

isco_list = []
name_list = []
for i, line in enumerate(lines88):


    if 'MAJOR GROUP' in line:
        
        x =  re.findall(r'\d+', line)[0]

        isco_list.append(x)
        name_list.append( format_func(lines88[i+1].strip() ) )



    elif len(re.findall(r'\d+', line)) == 1:
        number = re.findall(r'\d+', line)[0]
        

        # Strip removes leading and traling spaces and linebreaks (\n)
        # Replace And with and, because it is not consistent
        isco_list.append(number)
        name_list.append( format_func( line.replace(number,'')))

df88 = pd.DataFrame({'isco88': isco_list, 'isco88_name': name_list})

I = df88.duplicated()
I.sum() # None 

df88


df88['digits_level'] = df88.isco88.str.len()

look = df88[df88.digits_level==1]

look = df88[df88.digits_level==2]

look = df88[df88.digits_level==3]

look = df88[df88.digits_level==4]

I = df88.duplicated(subset='isco88',keep=False)
look = df88[I] # No duplicates in the isco88 version 

df88.to_csv('isco88_format_en.csv',index=False)
df88

# Read as object to preserve leading zeros
csv = pd.read_csv('isco88_format_en.csv',dtype='object')
csv