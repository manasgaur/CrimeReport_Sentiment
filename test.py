import json
#from pattern.en import sentiment
from dateutil import parser
from pattern.en import sentiment

import os
import datetime
print "task 1"

def main():
    print "hello world"

if __name__ == '__main__':
    main()

print "task 2"

list1=[1,2,3,4,5]

print "List=",list1

print "task 3"

out_file=open("list_data.txt","w")

json.dump(list1,out_file)

out_file.close()

in_file=open("list_data.txt","r")

new_data=json.load(in_file)

in_file.close()

print "List printed after taken from list_data.json"
print new_data

print "task 4"

list2=[6,7,8,9,10]
out_file=open("list_data.txt","w")

#list1.append(list2);
majorlist=dict()
newdata=dict()
majorlist["item1"]=list1
majorlist["item2"]=list2
#for i in range(0,len(list1))
json.dump(majorlist,out_file)

out_file.close()

in_file=open("list_data.txt","r")

new_data=json.load(in_file)

print "items1:",new_data["item1"]
print "items2:",new_data["item2"]

in_file.close()

print "task 5"

data=dict()
data['school']='Albany'
data['address']='1400 Washington Avenue, Albany NY 12222'
data['phone']='(518) 442-3300'

print data

#print "Values in data : %s" % data.keys()
print "keys or fields in data : ", data.keys()
print "Items in data : ", data.items()
print  "Values in data: ", data.values()

json.dump(data,open('dictionary.txt','w'))

data2=json.load(open('dictionary.txt'))

print "task 6.1"
print "keys:", data2.keys()
print "Items:", str(data2.items())
print "Values", str(data2.values())

in_file=open('multifile.txt','w')

in_file.write(str(data))
in_file.write('\n')
in_file.write(str(list1))

in_file.close()

print "task 6.2"
with open('multifile.txt','r') as f:
    line=f.readline()
    print line
    line=f.readline()
    print line

in_file=open('/Users/manasgaur/Desktop/MyApp/Chen_Python_work/Data_folder/CrimeReport.txt','r')
dataCR=[]

for line in in_file:
    temp=json.loads(line)
    dataCR.append(temp)

print "task 7"
print "following are the twitter ids"
for i in range(0,len(dataCR)):
    print dataCR[i]["id"]

print "task 8"

datelist=[]

for i in range(0,len(dataCR)):
    dt=parser.parse(dataCR[i]["created_at"])
    datelist.append(dt)

print "dates of the 10 recent tweets"
sorted_datelist=sorted(datelist)
recent_tweets=[]
for i in range(len(datelist)-10,len(datelist)):
    recent_tweets.append(str(sorted_datelist[i]))
    print sorted_datelist[i]
    print "\n"

op_file=open('output.txt','w')
for i in range(0,len(dataCR)):
    dtobj=parser.parse(dataCR[i]['created_at'])
    if (str(dtobj) in recent_tweets):
        json.dump(dataCR[i],op_file)
        op_file.write("\n")

op_file.close()
print "check output.txt file for recent tweets"

print "task 9"
for i in range(0,len(dataCR)):
    val=dataCR[i]["created_at"]
    dt=parser.parse(val)
    filename= str(dt.month)+"-"+str(dt.day)+"-"+str(dt.year)+"-"+str(dt.hour)+".txt"
    if (os.path.isfile(filename)):
        with open(filename,'a') as fi:
            fi.write('\n')
            json.dump(dataCR[i],fi)
    else:
        out_file=open(filename,'w')
        json.dump(dataCR[i],out_file)

out_file.close();

print "created files for separate tweets"






























import json
#from pattern.en import sentiment
from dateutil import parser
from pattern.en import sentiment

import os
import datetime
print "task 1"

def main():
    print "hello world"

if __name__ == '__main__':
    main()

print "task 2"

list1=[1,2,3,4,5]

print "List=",list1

print "task 3"

out_file=open("list_data.txt","w")

json.dump(list1,out_file)

out_file.close()

in_file=open("list_data.txt","r")

new_data=json.load(in_file)

in_file.close()

print "List printed after taken from list_data.json"
print new_data

print "task 4"

list2=[6,7,8,9,10]
out_file=open("list_data.txt","w")

#list1.append(list2);
majorlist=dict()
newdata=dict()
majorlist["item1"]=list1
majorlist["item2"]=list2
#for i in range(0,len(list1))
json.dump(majorlist,out_file)

out_file.close()

in_file=open("list_data.txt","r")

new_data=json.load(in_file)

print "items1:",new_data["item1"]
print "items2:",new_data["item2"]

in_file.close()

print "task 5"

data=dict()
data['school']='Albany'
data['address']='1400 Washington Avenue, Albany NY 12222'
data['phone']='(518) 442-3300'

print data

#print "Values in data : %s" % data.keys()
print "keys or fields in data : ", data.keys()
print "Items in data : ", data.items()
print  "Values in data: ", data.values()

json.dump(data,open('dictionary.txt','w'))

data2=json.load(open('dictionary.txt'))

print "task 6.1"
print "keys:", data2.keys()
print "Items:", str(data2.items())
print "Values", str(data2.values())

in_file=open('multifile.txt','w')

in_file.write(str(data))
in_file.write('\n')
in_file.write(str(list1))

in_file.close()

print "task 6.2"
with open('multifile.txt','r') as f:
    line=f.readline()
    print line
    line=f.readline()
    print line

in_file=open('/Users/manasgaur/Desktop/MyApp/Chen_Python_work/Data_folder/CrimeReport.txt','r')
dataCR=[]

for line in in_file:
    temp=json.loads(line)
    dataCR.append(temp)

print "task 7"
print "following are the twitter ids"
for i in range(0,len(dataCR)):
    print dataCR[i]["id"]

print "task 8"

datelist=[]

for i in range(0,len(dataCR)):
    dt=parser.parse(dataCR[i]["created_at"])
    datelist.append(dt)

print "dates of the 10 recent tweets"
sorted_datelist=sorted(datelist)
recent_tweets=[]
for i in range(len(datelist)-10,len(datelist)):
    recent_tweets.append(str(sorted_datelist[i]))
    print sorted_datelist[i]
    print "\n"

op_file=open('output.txt','w')
for i in range(0,len(dataCR)):
    dtobj=parser.parse(dataCR[i]['created_at'])
    if (str(dtobj) in recent_tweets):
        json.dump(dataCR[i],op_file)
        op_file.write("\n")

op_file.close()
print "check output.txt file for recent tweets"

print "task 9"
for i in range(0,len(dataCR)):
    val=dataCR[i]["created_at"]
    dt=parser.parse(val)
    filename= str(dt.month)+"-"+str(dt.day)+"-"+str(dt.year)+"-"+str(dt.hour)+".txt"
    if (os.path.isfile(filename)):
        with open(filename,'a') as fi:
            fi.write('\n')
            json.dump(dataCR[i],fi)
    else:
        out_file=open(filename,'w')
        json.dump(dataCR[i],out_file)

out_file.close();

print "created files for separate tweets"






























