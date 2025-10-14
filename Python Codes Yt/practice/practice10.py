"""i = 0
while i <= 5:
    if(i == 3):
        i += 1           
        continue
    print(i)
    i += 1"""

'''i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1   # to print odd numbers        
        continue
    print(i)
    i += 1'''



i = 0
while i <= 5:
    if(i % 2 != 0):
        i += 1        # to print even numbers
        continue
    print(i)
    i += 1