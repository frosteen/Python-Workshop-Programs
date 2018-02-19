num=input("Input a number: ")
sum=num
for i in range(1,num):
    sum=sum*(num-i)
print 'The factorical of', num, 'is', sum
input()
