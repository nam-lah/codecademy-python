
# square list for even numbers only in a range of 1-12
[x**2 for x in range(1,12) if (x) % 2 == 0]

# list of doubles for numbers divisible by three, range of 1-6
[x*2 for x in range(1,6) if (x*2) % 3 == 0]

# other comprehension list
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 ==0]
print cubes_by_four

# 7 List slicing
l = [i ** 2 for i in range(1, 11)]
# will print  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
# will print [9, 25, 49, 81]


# 8. Omitting indexes.
my_list = range(1, 11) # List of numbers 1 - 10

# will print with from beginning to end with a stride of three numbers.
print my_list[::3]

# negative striding, reverse listing
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
