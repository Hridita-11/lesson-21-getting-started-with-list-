l=[4,5,1,2,9,7,10,8]
print("original list",l)
count=0
for i in l:
    count +=i
avg= count/len(l)
print("sum=",count)
print("avarage=",avg)
l.sort()
print("Smallest element is:",l[0] )
print("Largest elementis:",l[-1])