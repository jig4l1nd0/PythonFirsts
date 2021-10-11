#append() - Add an element to the end of the list
#extend() - Add all elements of a list to the another list
#insert() - Insert an item at the defined index
#remove() - Removes an item from the list
#pop() - Removes and returns an element at the given index
#clear() - Removes all items from the list
#index() - Returns the index of the first matched item
#count() - Returns the count of the number of items passed as an argument
#sort() - Sort items in a list in ascending order
#reverse() - Reverse the order of items in the list			
#copy() - Returns a shallow copy of the list

# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

##########################
### List Comprehension ###

pow2 = [2 ** x for x in range(10)]
print pow2 

# that is equivalent to
pow2 = []
for x in range(10):
   pow2.append(2 ** x)

pow2 = [2 ** x for x in range(10) if x > 5]
print pow2


odd = [x for x in range(20) if x % 2 == 1]
print odd

#output ['Python Language', 'Python Programming', 'C Language', 'C Programming']
CodinPy = [x+y for x in ['Python ','C '] for y in ['Language','Programming']] 

#######################
### List membership ###

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# Output: True
print 'p' in my_list

# Output: False
print 'a' in my_list 

# Output: True
print 'c' not in my_list  

