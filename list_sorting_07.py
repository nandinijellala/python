#sorting techniques

#method 1

a=[23,1,10,5,2]
i=0
j=0
count=0
while(i<len(a)):
    j=0
    temp=0
    while(j<len(a)):
      if(a[i]<a[j]):
        temp=a[j]
        a[j]=a[i]
        a[i]=temp
      count=count+1
      j=j+1
    i=i+1
print(a)
print(f"count={count}")
print("")

#method 2(bubble sort)

a=[23,1,10,5,2]
i=0
count=0
while(i<len(a)):
    j=i+1
    temp=0
    while(j<len(a)):
        if(a[i]>a[j]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
        count=count+1
        j=j+1
    i=i+1
print(a)
print("count=",count)

#note:no of iterations will get decreased in method 2 when compared to method 1
#method 3(insertion sort)
a=[23,1,10,5,2]
i=1
count=0
while(i<5):
    j=i-1
    key=a[i]
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j=j-1
        count=count+1
    a[j+1]=key
    i=i+1
print(a)
print("count={}".format(count))
#note:no of intersections will get decreased in method 3 when compared to method 2
#and method 1
        
