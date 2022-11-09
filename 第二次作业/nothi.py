import os
import re

data_dir = 'sentiment'
trainTextPath = data_dir + os.sep + "train_text.txt"
f = open(trainTextPath, mode="r", encoding="utf-8")
textList = f.read().lower().strip()  # .split("\n")
textList = textList.split("\n")
print(len(textList))
newList = []
pp=1
for itm in textList:
    print(itm)
    itm=re.sub(r"http[^ ]*", " ", itm)
    newList.append(itm)
    print(itm)
    pp+=1
    if pp>=500:
        break
# textList=[]

