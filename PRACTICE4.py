fileText=open('DNA.txt')
total=0
length=0
for char in fileText.read():
    if char=='C' or char=='G':
        total=total+1
    length=length+1.0
print "The percent of C+G is",total/length*100
