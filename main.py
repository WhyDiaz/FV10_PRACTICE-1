from pyscript import document, display

#x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#del x[4]
#display(x)  # deletes Friday from the list

#del x[2]  # deletes Thursday from the list
#x.remove('Friday')  # removes Friday from the list
#display(x)  # displays the updated list without Thursday and Friday

#In del you can use the index of the element you want to delete, while in remove() you can use the value of the element you want to remove.

#x.pop()  # removes the last element from the list cuz nothing is specified in the parentheses, more flexible than del and remove because it can take both index and value
#display(x)

#.clear()
#display(x) # clears the ENTIRE list 

#sort() - arranges items in asecending order (A - Z or smallest to largest)
#reverse() - reverses the order of tiems in a list 
#sorted() - returns a new sorted list without changing the original list

#x.sort()  # sorts the list in ascending order
#display(x)  # displays the sorted list

#x.reverse()  # reverses the order of the list
#display(x)  # displays the reversed list

#numbers = [3,1,2] -> [1,2,3]
#display(sorted(numbers))  # displays a new sorted list without changing the original list
#display(numbers)  # displays the original list without any changes

#The difference betweeen a method and a function
#The method operates on the data in the class, while a function is usd to return or passs the data. 

#dogs = {"Pommeranian", "Labrador", "Golden Retriever",}
#dogs.add("Husky")  # creates a new set with "Husky"
#display(dogs)


#sample_set = {} # data type is a dictionary, however if a value is present it is a set
#display(type(sample_set))






A = {'soda', 'candy', 'chocolate','burger', 'soda'}
B = {'cotton candy', 'burger', 'fries'}
C = {'chicken nuggets'}

#display(A | B | C)  # displays the union of sets A and B
#display(A | B | C)  # displays the union of sets A, B, and C

#display(union(A, B))  # displays the union of sets A and B
#display(A.union(B, C))  # displays the union of sets A, B, and C

#display(A&B)  # displays the intersection of sets A and B {'burger'}
#display(A&C) # displays the intersection of sets A and C set() - empty set becasue there is no common element between A and C

#display(A.intersection(B, C))  # displays the intersection of sets A, B, and C set() - empty set because there is no common element between A, B, and C

#display(A-B)  # displays the difference of sets A and B {'soda', 'candy', 'chocolate'}

#display(A^B)  # displays the symmetric difference of sets A and B {'soda', 'candy', 'chocolate', 'cotton candy', 'fries'}

