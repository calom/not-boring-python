In this chapter, I’ll discuss the basics of lists. I’ll also teach you about methods, which are functions that are tied to values of a certain data type. Then I’ll briefly cover the sequence data types (lists, tuples, and strings) and show how they compare with each other. In the next chapter, I’ll introduce you to the dictionary data type.

List:
- multiple values ordered sequence
- can change values at index
- example: ['cat', 'bat', 'rat', 'elephant']
- comma-delimited 


Negative value
- '-1' index is last item, higher number means further from end until last 
or 'list index out of range'

Slices 
- list[x:x], 

Length of list
- fun: len(list_name) 

List concatenation and replication
- concatenate using '+' symbol
    - to extend the list, name of the list + extra new item and assign it to the original list like `list = list + new_item`
- replicate using '*' symbol 


Deleting items from list 
- fun: del list_name[item_index]

Using lists, fun: range() and for loop:
- range(int) returns sequence of integers from 0 to int-1
- common practice is using range(len(list_name))

Operators 'in' and 'not in'
- ealuates to boolean value (true or false)

Multiple assignment trick
- assign multiple values in one statement, assigning them to a list of values
- order matters, number of values must match lenght of the list, othervise "ValueError"
- example: 
    - cat = ['fat', 'gray', 'loud']
    - size, color, disposition = cat

Fun: enumerate()
- enumerate returns index of item + value of the item at the index
- example:  
        for index, item in enumerate(supplies):
         print('Index ' + str(index) + ' in supplies is: ' + item)

Lists with function random.choice() and random.shuffle()
- functions that accepts list as argument
- random.choice(list_name) returns random item from list
- random.shuffle(list_name) reorders list items

Augmented assignment operator 
- operators are:
    - +=  
    - -=
    - *=
    - /=
    - %=

Methods following with examples of some
- method is same as fun: but it is called upon value with '.' symbol

Method index() - finding value with index
- list_name.index(value) = if value is there it returns index of it, otherwise 'ValueError' error
- if same more than 1 item of same value in the list = 1st index returned

Adding values - append() and insert()
- those are list methods only (not for strings, integers)
- list.append(item) = adds new item afetr last index 
- list.insert(index, item) = adds value at an index moving forward all other items from that index further

Removing with remove()
- list.remove(item_value)
- ValueError if not in list
- if multiple times, 1st is deleted

METHOD sort()
- attributes to pass: 
    - reverse=true ... reversed order  e.g. list.sort(reverse=true)
    - can't compare mixed types of values in single list (int and strings together, python doesnt know how to compare)
    -  ASCIIbetical order is used .... uppercase is before lowercase 
    - sorting in regular alphabetical order 
        - >>> spam = ['a', 'z', 'A', 'Z']
          >>> spam.sort(key=str.lower)

Lists and indentation exception
- until list is finished with ']' I can use whatever indentation and python counts it still as being withing of list definition

Reverse order
- list.reverse() method does that

String and lists are similar -> String is sequence of chars so...

Mutable and Immutable data types
- list is MUTABLE ... can change, add or remove values
- String is IMMUTABLE ... cant change values or add,remove
- to mutate String you have to use old String var with slice and modify to assign to a new variable 

Tupple - the immutable list
- defined with '()' instead of '[]'
- values cannot be modified
- trailing comma ... I can define tupple with defining one or two value and trailing comma with blank)

list() and tuple() fun - converting values

Referencing:
- when var1=list[ ] it creates list value as reference and assign it to a var1
- when var2=var1 that means var 2 now equals to same reference ....chanign particular value "of" var2 changes also var1, as this changes reference, otherwise original...reference is coppied, not value

Identity and id() function
- with lists, append() changes reference, calling it 'moifying object in-place'

Function copy() and deepcopy()
- module 'copy'
- copy.copy() ... make duplicate copy of mutable value (not ref.)
- if list in copy contains other lists use deepcopy
