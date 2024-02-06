strr=input("Enter the string: ")
cnt=0
strcnt=[]
print(len(strr))
for i in range(len(strr)):
    #print(str[i])
    for j in range(len(strr)):
        if strr[i]==strr[j]:
            cnt +=1
            count=cnt
    strcnt.append(strr[i]+str(count))   
    cnt=0

strcnt=set(strcnt)
print(''.join(map(str,strcnt)))
#print(strcnt)   
