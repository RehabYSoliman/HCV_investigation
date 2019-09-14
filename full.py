

# In[21]:


def Fisolate_source(record):
    isolation_source=[]
    country=[]
    version=[]
    
    for l in record:
                if l.startswith('VERSION'):
                    version=version+[l[12:]]
                    countV+=1
                if l.startswith('/isolation_source'):
                    isolation_source=isolation_source+[l[19:-1]]
                else:   
                    if l.startswith('/country'):
                        country=country+[l[10:-1]]
                total=(country,countS,countV,count_C)
    return (version,isolation_source ) 


# In[22]:


record = []
R=[]
for x in dataSource:
    filh=open(x)
    for line in filh:
        line=line.lstrip()
        line=line.rstrip()
        if not line.startswith('//'):
            record.append(line)
        else:
            R=R+[(Fisolate_source(record))]
            record = []
            continue
print(R)


