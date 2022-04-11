def eggs(someParam):
    print(id(someParam))
    someParam.append('Hello')

spam = [1,2,3]

eggs(spam)
print(id(spam))
print(spam)