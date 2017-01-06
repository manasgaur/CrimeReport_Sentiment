import json
import os
import sys
from pattern.en import sentiment,positive

#reload(sys)

# when you run this code make sure you put the correct location of file: CrimeReport.txt
in_file=open('/Users/manasgaur/Desktop/MyApp/Chen_Python_work/Data_folder/CrimeReport.txt','r')
tweets=[]
for line in in_file:
    tweet=json.loads(line)
    tweets.append(tweet)

in_file.close()

for i in range(len(tweets)):
    val=tweets[i]["text"]
    if positive(val,threshold=0.1):
       if os.path.isfile('positive.txt'):
           with open('positive.txt','a') as pos:
                pos.write("Text")
                json.dump(val,pos)#pos.write(str(val))
                pos.write('\n')
                pos.write('\n')
                pos.write("Sentiment Assessment:\n")
                l=sentiment(val).assessments
                json.dump(l,pos)
                pos.write('\n')
                pos.write('\n')
                #pos.close()
       else :
           in2_file=open('positive.txt','w')
           in2_file.write("Text")
           json.dump(val,in2_file)
           in2_file.write('\n')
           in2_file.write('\n')
           in2_file.write("Sentiment Assessment:\n")
           l=sentiment(val).assessments
           json.dump(l,in2_file)
           in2_file.write('\n')
           in2_file.write('\n')
           in2_file.close()
    else:
        if os.path.isfile('negative.txt'):
           with open('negative.txt','a') as neg:
                neg.write("Text")
                json.dump(val,neg)#neg.write(str(val))
                neg.write('\n')
                neg.write('\n')
                neg.write("Sentiment Assessment:\n")
                l=sentiment(val).assessments
                json.dump(l,neg)
                neg.write('\n')
                neg.write('\n')
                #neg.close()
        else :
           in3_file=open('negative.txt','w')
           json.dump(val,in3_file)
           in3_file.write('\n')
           in3_file.write('\n')
           in3_file.write("Sentiment Assessment:\n")
           l=sentiment(val).assessments
           json.dump(l,in3_file)
           in3_file.write('\n')
           in3_file.write('\n')
           in3_file.close()