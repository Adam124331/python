
string = "xyz"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))


------------------------------------------------------------


# Sample built-in iterators
 
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")   
s = "Geeks"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")  
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))

------------------------------------------------------------
tup = ('a', 'b', 'c', 'd', 'e')
 
# creating an iterator from the tuple
tup_iter = iter(tup)
 
print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
    print(item)
 
    # break outside loop after iterating on 3 elements
    if index == 2:
        break
 
# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))


---------------------------------------------------------------------

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
