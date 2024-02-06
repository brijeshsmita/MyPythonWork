# numbers = [50,2,1,9]

numbers=[int(x) for x in input().split()]
#accepting values from user into a list
print("original list:", numbers)

numbers.sort()
print("sorted list: ", numbers)

strr=""
for i in range(len(numbers)):
               strr=strr+str(numbers.pop())
print(strr)

'''
ans=[]
for i in range(len(numbers)-1,-1,-1):
#parameter1: range, p2: starting value, p3:increment or decrement by
#for i in range(len(numbers)):
# starts from 0th index and increments forward that generates '12950'
    ans.append(numbers[i])
print(''.join(map(str,ans)))
'''
    
