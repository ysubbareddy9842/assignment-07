my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(my_data)

# elements from 3rd to 5th
# prints (33, 44, 55)
print(my_data[2:5])

# elements from start to 4th
# prints (11, 22, 33, 44)
print(my_data[:4])

# elements from 5th to end
# prints (55, 66, 77, 88, 99)
print(my_data[4:])

# elements from 5th to second last
# prints (55, 66, 77, 88)
print(my_data[4:-1])

# displaying entire tuple
print(my_data[:])