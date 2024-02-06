dict={
    "merry":"god",
    "christmas":"jul",
    "and":"och",
    "happy":"gott",
    "new":"nytt",
    "year":"ar"
    }

# lst=["Christmas", "NEw"]
# design time values

lst=[x for x in input("Enter your wish: ").split()]
#accepting values from user into a list

wish=""
for itm in lst:
    itmcs=itm.casefold()   #casefold() is used for case insensitive search
    if itmcs in dict:
        wish=wish + " "+dict[itmcs]
print(wish)
