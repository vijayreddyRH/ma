m1 = int(input("Enter the marks in the first test: "))
m2 = int(input("Enter the marks in second test: "))
m3 = int(input("Enter the marks in third test: "))
if (m1 > m2):
 if (m2 > m3):
 total = m1 + m2
 else:
 total = m1 + m3
elif (m1 > m3):
 total = m1 + m2
else:
 total = m2 + m3
Avg = total / 2
print("The average of the best two test marks is: ", Avg)






/////////////////
temp=num
rev=0
while(num!=0):
 rem=num%10
 rev=rev*10+rem
 num=num//10
 if rem == digit:
 count += 1
if temp==rev:
 print("The number is a palindrome!")
else:
 print("The number isn't a palindrome!")
print("{} occurred {} times in {}".format(digit, count, temp))
