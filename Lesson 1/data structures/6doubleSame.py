def same_digits(n,d):
    if sorted(str(n))== sorted(str(d)):
        print ("{0} and {1} contain same digits and same length" . format(n,d))
        #print(n, " and ", d," are same")
    else:
        print ("{0} and {1} do NOT contain same digits and same length" . format(n,d))


num=int(input("enter a number: "))        #accept a number
dbl=num*2               #double of number
print(dbl)

same_digits(num,dbl)


#input: 125874
#double: 251748
