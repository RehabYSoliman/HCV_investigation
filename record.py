#!/usr/bin/env python
# coding: utf-8

# In[19]:

def process_record (record):
    #record=open(file_name)
    #count=0
    new_record= {'Accession':[],'Strain':[],'Pubmed':[],'genotype':[]}
    
    for i in record:
        i=i.lstrip()
        if i.startswith('ACCESSION'):
            x=i.split()
            new_record['Accession']=new_record['Accession']+[x[1]]
        else:
            if i.startswith('/strain='):
                new_record['Strain']=new_record['Strain']+[i[9:-1]]
            else:
                if i.startswith('PUBMED'):
                    new_record['Pubmed']=new_record['Pubmed']+[i[8:-1]]
                else:
                    if i.startswith('/note='):
                        x=i.find('gen')
                        if x>0:
                            i=i[x:-1]
                            y=i.split(':')
                            new_record['genotype']=new_record['genotype']+[y[-1]]
    return  new_record;


# In[6]:


dataSource=['EgyptianNotEgypt.gb','EgyptNotEgyptian.gb']
record = []
for x in dataSource:
    filh=open(x)
    for line in filh:
        line=line.lstrip()
        line=line.rstrip()
        if (not line.startswith('//')):
#             print(line)
            record.append(line)
        else:
            result=process_record(record)
            continue
print(result)

        #for i in record :print (i)






