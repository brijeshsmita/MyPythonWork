lst=[int(x) for x in input("enter the numbers: ").split()]
num=int(input("Amount to be matched: "))
cnt=0

for i in lst:
    if i<num:
        for j in lst:
            print(i, j)
            if i+j == num:
                cnt +=1
print("count: ", int(cnt/2))
        
