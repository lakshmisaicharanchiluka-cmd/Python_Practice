# write a programe to search for a number x in this tuple using loop
# (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

num = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100)

x = 81

i = 0
while i <len((num)):
    if(num[i] == x ):
        print("Found At idx  ",  i)
    else:
        print(" Finding...... ")
    i += 1