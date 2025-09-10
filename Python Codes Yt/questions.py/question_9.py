a = int(input("Enter The First Number  :  "))
b = int(input("Enter The Second Number  :  "))
c = int(input("Enter The Third Number  :  "))
if(a > b and a > c):
    print("The Greatest Number Is  ->  " , a)
elif(b > c and b > a):
    print("The Greatest Number Is  ->  " , b)
else:
    print("The Greatest Number Is  ->  " , c)