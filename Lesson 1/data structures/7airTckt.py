psngr=int(input("How many passengers? "))
airline=input("Enter Airlines: ")
src =input("Enter Source: ")
dest =input("Enter Destination: ")

print("Ticket Details:::")

tckts=[]
tcktnum=101
i=0

while i < psngr:
    #print(airline+":"+src[:3]+":"+dest[:3]+":"+str(tcktnum))
    tckts.append(airline+":"+src[:3]+":"+dest[:3]+":"+str(tcktnum))
    tcktnum=tcktnum+1
    i+=1
print(tckts)
print("Only first 3 tckts: ", tckts[:3]) #first 3 items
print("Only last 3 tckts: ", tckts[psngr-3:psngr]) # last three items


