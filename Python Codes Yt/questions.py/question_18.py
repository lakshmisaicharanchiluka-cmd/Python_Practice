'''write a programe to search for a number x in this tuple using loop
(1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)'''

# using while loop

num = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

'''x = 25

i = 0
while i <len((num)):
    if(num[i] == x ):
        print("Found At idx  ",  i)
        break                               # linear search
    else:
        print(" Finding...... ")
    i += 1'''


    # using for loop

x = 49
idx = 0
for i in num:
    if(i == x):
        print("Number Found At idx"  , idx)
    idx += 1