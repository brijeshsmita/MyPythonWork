numbers=[int(x) for x in input("enter numbers: ").split()]
#accepting values from user into a list
print("Numbers in the List: ", numbers)
cnt=0
for i in range(len(numbers)-1):
    if(numbers[i]==numbers[i+1]):
        print(numbers[i] , " & " , numbers[i+1])
        cnt+=1
print(cnt)
   
   
#input: 3 1 2 2 3 1 1
#input: 11 22 22 34 56 56

