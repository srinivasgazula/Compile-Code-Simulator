# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:27:11 2021

@author: jeevan
"""

with open("inputvector.txt") as f:
    content_list = f.readlines()

# print the list
# remove new line characters
content_list = [x.strip() for x in content_list]
while("" in content_list) :
    content_list.remove("")
# print(content_list)
inputvector=content_list
# print(inputvector)
inputstring=""
inputlist=[]
nodes={}
count=1
with open("source.txt") as f:
    content_list = f.readlines()

# print the list
# remove new line characters
content_list = [x.strip() for x in content_list]
while("" in content_list) :
    content_list.remove("")

# for i in content_list:
#     i=i.replace(" ", "")
#     print(i)
# print(content_list)

for i in range(0,len(content_list)):
    content_list[i]=content_list[i].replace(" ","")
source=content_list

for i in source:
    if(i[0:5]=="input"):
        inputstring=i[5:]
        break
# print(inputstring)
stri=""
for i in inputstring:
    if(i==';'):
        inputlist.append(stri)
        break
    elif(i==','):
        inputlist.append(stri)
        stri=""
    else:
        stri=stri+i
# print(inputlist)
# print(source)
for i in range(0,len(source)):
    # print(i)
    a=source[i]
    if((a.find("AND2X1"))!=-1):
        nodes[count]=["AND2X1",a]
        count=count+1
    if((a.find("INVX1"))!=-1):
        nodes[count]=["INVX1",a]
        count=count+1
    if((a.find("OR2X1"))!=-1):
        nodes[count]=["OR2X1",a]
        count=count+1
    if((a.find("NAND2X1"))!=-1):
        nodes[count]=["NANDX1",a]
        count=count+1
    if((a.find("NOR"))!=-1):
        nodes[count]=["NOR2X1",a]
        count=count+1
    if((a.find("XOR2X1"))!=-1):
        nodes[count]=["XOR2X1",a]
        count=count+1
    if((a.find("BUFX1"))!=-1):
        nodes[count]=["BUFX1",a]
        count=count+1
# print(count)
# print(nodes)    
    
for key in nodes:
    a=nodes[key][1]
    b=a.find("(")
    c=a[b+1:-2]
    nodes[key].append(c)
# print(nodes)
string=""
complist=[]
for key in nodes:
    a=nodes[key][2]
    for i in a:
        if("(") in complist:
            if(i!=")"):
                string=string+i
                # print(string)
            else:
                nodes[key].append(string)
                string=""
                complist=[]
        if(i=="("):
            complist.append(i)
            # print(complist)
for key in nodes:
    nodes[key].pop(1)
    nodes[key].pop(1)
# print(nodes)
        
node={}
for key in nodes:
    a=nodes[key]
    node[key]=[a,[],[],[]]
# print(node)

#########
priinputs=inputlist
nodes=node
# print(priinputs)
# print(nodes)
###############
l1=[]
level={}
for i in priinputs:
    level[i]=0
valueslist={}
result={'AND2X1':{"00":'0',"01":'0',"10":'0',"11":'1'},'OR2X1':{"00":'0',"01":'1',"10":'1',"11":'1'},'INVX1':{'0':'1','1':'0'},
        'NAND2X1':{"00":'1',"01":'1',"10":'1',"11":'0'},'NOR2X1':{"00":'1',"01":'0',"10":'0',"11":'0'},'XOR2X1':{"00":'0',"01":'1',"10":'1',"11":'0'},'BUFX1':{'0':'1','1':'0'}}

for key in nodes:
    compare=nodes[key][0][1]
    for keysecond in nodes:
        if(keysecond!=key):
            a=nodes[keysecond][0]
            for i in range(2,len(a)):
                if(a[i]==compare):
                    nodes[key][1].append(keysecond)
                    break
for key in nodes:
    a=nodes[key][0]
    for i in range(2,len(a)):
        if(a[i] not in priinputs):
            nodes[key][2]=0
            break
        else:
            nodes[key][2]=1 

for key in nodes:
    if(nodes[key][2]==1):
        a=nodes[key][0]
        # print(a)
        level[a[1]]=1
        # for i in range(2,len(a)):
        #     level[a[i]]=0

for i in range(0,len(nodes)):
    for key in nodes:
        if(nodes[key][2]==0):
            b=nodes[key][0]
            for j in range(2,len(b)):
                if b[j] not in level.keys():
                    l1=[]
                    break
                else:
                    l1.append(level[b[j]])
                    # print(l1)
                if(j==len(b)-1):
                    # print(max(l1)+1)
                    level[b[1]]=max(l1)+1
                    #print(level)
                    nodes[key][2]=max(l1)+1
levelmax=max(level.values())
# print(nodes)

print("The input list of the circuit is ",priinputs)
print("\nThe level of this circuit is\n ",levelmax)

for j in inputvector:
    # print(j)
    levelno=1
    markedlist=[]
    for i in range(0,len(priinputs)):
        # print(j[i])
        valueslist[priinputs[i]]=j[i]
    while(levelno<=levelmax):
        for key in nodes:
            if key not in markedlist:
                if(nodes[key][2]==levelno):
                    if((nodes[key][0][0]=="AND2X1") or (nodes[key][0][0]=="OR2X1") or (nodes[key][0][0]=="NAND2X1") or (nodes[key][0][0]=="NOR2X1") or (nodes[key][0][0]=="XOR2X1")):
                        for i in result:
                            if(i==nodes[key][0][0]):
                                t=result[i]
                                a=valueslist[nodes[key][0][2]]+valueslist[nodes[key][0][3]]
                                output=t[a]
                                nodes[key][3]=output
                                # print(output)
                                valueslist[nodes[key][0][1]]=output
                    else:
                        for i in result:
                            if(i==nodes[key][0][0]):
                                t=result[i]
                                a=valueslist[nodes[key][0][2]]
                                output=t[a]
                                nodes[key][3]=output
                                valueslist[nodes[key][0][1]]=output
                    markedlist.append(key)
                #node[key][3]=output
                #valueslist[key[0][1]]=output
        levelno=levelno+1
    print("For input vector of ",j," The values of all variables are\n ")
    print(valueslist,"\n")



      