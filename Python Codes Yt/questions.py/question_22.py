# write a programe to find the factorial of first n numbers using for loop

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i                    # using while loop
    i += 1

print("Factorial  = ", fact)


n = 5
fact = 1
for i in range(1, n+1):                     #  using for loop
    fact *= i

print("Factorial  = ", fact)
