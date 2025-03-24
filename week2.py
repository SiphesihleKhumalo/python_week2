# Step 1: Create an empty list
numbers_list = []  

#Step 2: Append the elements
numbers_list.append(10)
numbers_list.append(20)
numbers_list.append(30)
numbers_list.append(40)
numbers_list.append(50)

# Step 3: Insert 15 at the second position (index 1)
numbers_list.insert(1, 15)  

# Step 4: Extend the list with [50, 60, 70]
numbers_list.extend([50, 60, 70])

# Step 5: Remove the last element
numbers_list.pop() 

# Step 6: Sort the list in ascending order
numbers_list.sort()

# Step 7: Find and print the index of value 30
index_30 = numbers_list.index(30)  # Finds the index of 30
print("Index of 30:", index_30) 

# Print the final list
print("Final List:", numbers_list)