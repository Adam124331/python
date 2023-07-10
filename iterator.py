iter method by using iter nad next function
val=1,2,5,3
n=iter(val)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())

-----------------------------------------------------------
iter method by using next try catch method
val ="python"
n=iter(val)
while True:
    try:
        word=next(n)
        print(word)
    except StopIteration:
        exception will happen when iteration is over
        break

---------------------------------------------------------
#generator function
def simplefunction():
    yield 1 #A generator function that yields 1 for first time,
             4 second time and 5 third time
    yield 4
    yield 5
------------------------------------------------------
#for i in simplefunction():
    #print(i)
#generator funtion using  next keyword
#generator funtion
def simplefunc():
    yield 1
    yield 2
    yield 3
    #n is an generator object
n = simplefunc()
    #iteration over generator by using next keyword()
print(next(n))
print(next(n))
print(next(n))
