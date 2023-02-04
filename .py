# Lists


Lists
Indexing
We are going to take a look at lists in Python. A list is a sequenced collection of different objects such as integers, strings, and other lists as well. The address of each element within a list is called an index. An index is used to access and refer to items within a list.

Image
To create a list, type the list within square brackets [ ], with your content inside the parenthesis and separated by commas. Let’s try it!

# Create a list
​
L = ["Michael Jackson", 10.1, 1982]
L
['Michael Jackson', 10.1, 1982]
We can use negative and regular indexing with a list :

Image
# Print the elements on each index
​
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )
the same element using negative and positive indexing:
 Postive: Michael Jackson 
 Negative: Michael Jackson
the same element using negative and positive indexing:
 Postive: 10.1 
 Negative: 10.1
the same element using negative and positive indexing:
 Postive: 1982 
 Negative: 1982
List Content
Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:

# Sample List
​
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]
List Operations
We can also perform slicing in lists. For example, if we want the last two elements, we use the following command:

# Sample List
​
L = ["Michael Jackson", 10.1,1982,"MJ",1]
L
['Michael Jackson', 10.1, 1982, 'MJ', 1]
Image
# List slicing
​
L[3:5]
['MJ', 1]
We can use the method extend to add new elements to the list:

# Use extend to add elements to list
​
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L
['Michael Jackson', 10.2, 'pop', 10]
Another similar method is append. If we apply append instead of extend, we add one element to the list:

]
# Use append to add elements to list
​
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L
['Michael Jackson', 10.2, ['pop', 10]]
Each time we apply a method, the list changes. If we apply extend we add two new elements to the list. The list L is then modified by adding two new elements:

# Use extend to add elements to list
​
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L
['Michael Jackson', 10.2, 'pop', 10]
If we append the list ['a','b'] we have one new element consisting of a nested list:

# Use append to add elements to list
​
L.append(['a','b'])
L
['Michael Jackson', 10.2, 'pop', 10, ['a', 'b']]
As lists are mutable, we can change them. For example, we can change the first element as follows:

# Change the element based on the index
​
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
Before change: ['disco', 10, 1.2]
After change: ['hard rock', 10, 1.2]
We can also delete an element of a list using the del command:

# Delete the element based on the index
​
print('Before change:', A)
del(A[0])
print('After change:', A)
Before change: ['hard rock', 10, 1.2]
After change: [10, 1.2]
We can convert a string to a list using split. For example, the method split translates every group of characters separated by a space into an element in a list:

# Split the string, default is by space
​
'hard rock'.split()
['hard', 'rock']
We can use the split function to separate strings on a specific character. We pass the character we would like to split on into the argument, which in this case is a comma. The result is a list, and each element corresponds to a set of characters that have been separated by a comma:

# Split the string by comma
​
'A,B,C,D'.split(',')
['A', 'B', 'C', 'D']
Copy and Clone List
When we set one variable B equal to A; both A and B are referencing the same list in memory:

B = A
# Copy (copy by reference) the list A
​
A = ["hard rock", 10, 1.2]
B = A
print(A)
print(B)
['hard rock', 10, 1.2]
['hard rock', 10, 1.2]
Image
Initially, the value of the first element in B is set as hard rock. If we change the first element in A to banana, we get an unexpected side effect. As A and B are referencing the same list, if we change list A, then list B also changes. If we check the first element of B we get banana instead of hard rock:

# Examine the copy by reference
​
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])
B[0]: hard rock
B[0]: banana
This is demonstrated in the following figure:

Image
You can clone list A by using the following syntax:

# Clone (clone by value) the list A
​
B = A[:]
B
['banana', 10, 1.2]
Variable B references a new copy or clone of the original list; this is demonstrated in the following figure:

Image
Now if you change A, B will not change:

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
B[0]: banana
B[0]: banana
Quiz on List
Create a list a_list, with the following elements 1, hello, [1,2,3] and True.

t
# Write your code below and press Shift+Enter to execute
a_list = (1, 'hello', [1,2,3], 'True')
a_list
(1, 'hello', [1, 2, 3], 'True')
Double-click <b>here</b> for the solution.
​
<!-- Your answer is below:
a_list = [1, 'hello', [1, 2, 3] , True]
a_list
-->
Find the value stored at index 1 of a_list.

[1]
# Write your code below and press Shift+Enter to execute
a_list[1]
'hello'
Double-click <b>here</b> for the solution.
​
<!-- Your answer is below:
a_list[1]
-->
Retrieve the elements stored at index 1, 2 and 3 of a_list.

a_list[1:4]
# Write your code below and press Shift+Enter to execute
a_list[1:4]
('hello', [1, 2, 3], 'True')
Double-click <b>here</b> for the solution.
​
<!-- Your answer is below:
a_list[1:4]
-->
Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:

A + B
# Write your code below and press Shift+Enter to execute
A = [1, 'a']
B = [2, 1, 'd']
A + B
[1, 'a', 2, 1, 'd']
Double-click <b>here</b> for the solution.
​
<!-- Your answer is below:
A = [1, 'a'] 
B = [2, 1, 'd']
A + B
-->
