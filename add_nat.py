from sys import argv
script, n = argv
n = int(n)
num = 1
sum = 0

while num <= n:
    sum += num
    num += 1

print(f"The sum of the {n} natural numbers is {sum}")
 
