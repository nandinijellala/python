#global,local,non-local variables,closure
#local variable
'''
def show():
    a=5  #local variable for show funct
    print(a)
    a=a+10
def demo():
    a=50 #local variable for demo funct
    print(a)
show()
demo()
print(a)
'''
#global variable
'''
n=10
def show():
    global n
    print(n) #20
    n=n+10   #30
def demo():
    global n
    print(n) #300
    n=n*10   #3000
print(n) #10
n=n+10   #20
show()
n=n*10   #300
demo()
print(n) #3000
'''
#non local variable
'''
def outer():
    x=5
    def inner():
        nonlocal x
        print(x)
        x=x+10
    inner()
    print(x)
outer()
'''
'''
def show():
    return 10
a=show 
print(a) #adress of show funct is printed
print(show())
'''
#closure:when program has three properties-nested function,outer funct returns the
#adress of inner funct,inner funct should use outer funct variables then closure will work
'''
def outer():
    x=5
    def inner(y):
        return x+y
    return inner
a=outer()
print(a)
print(a(6))
'''
#function as argument to another function
'''
def add(x,y):
    return x+y
def summation(f,a,b):
    s=f(a,b)
    return s
print(summation(add,10,20))
'''
'''
def summation(nums1,nums2):
    print(sum(nums1)+sum(nums2))
def main(f,*args):
    print(args)
    print(*args)
    result=f(*args)
    print(result)
main(summation,[1,2,3,4,5],[6,7,8,9,10])
'''
'''
def display(*n):
    print(n)
    print(*n)
print(display(1,2,3))
'''
#function returning another function
'''
def add_two_nums(x,y):
    return x+y
def add_three_nums(x,y,z):
    return x+y+z
def getfunction(num_len):
    if num_len==3:
        return add_three_nums
    else:
        return add_two_nums
args=[10,20,30]
num_len=len(args)
result=getfunction(num_len)
print(result(*args))
'''               
