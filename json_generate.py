import random
import json
name=input("Enter Name for dataset : ")
row=int(input("Enter number of row : "))
col=int(input("Enter number of col : "))

col_name=[]
data=[] 

for i in range(col):
    a=[]
    a.append(input("Enter name of Column {} :".format(i)))
    val_type=int(input("Press 1 for Range OR Press 2 for List : "))
    a.append(val_type)
    if val_type==1:
        a.append(input("Enter starting of range : "))
        a.append(input("Enter ending of range : "))
        col_name.append(a)
    else:
        b=[]
        size=int(input("Enter the size of list : "))
        for i in range(size):
            b.append(input("Enter value {} : ".format(i)))
        a.append(b)
        col_name.append(a)        
    
        

print(col_name)                   
                     
for i in range(row):
    a=[]
    for i in range(col):
        if col_name[i][1]==1:
            start=int(col_name[i][2])
            end=int(col_name[i][3])
            a.append(random.randint(start,end))
        else:
            val_list=col_name[i][2]
            a.append(random.choice(val_list))
            
    data.append(a)

json_data={}
json_data[name]=[]
for i in range(row):
    a={}
    for j in range(col):
        column=col_name[j][0]
        row_data=data[i][j]
        a[column]=row_data

    json_data[name].append(a)

print(json_data)
with open('man.json', 'w') as outfile:
    json.dump(json_data, outfile)
