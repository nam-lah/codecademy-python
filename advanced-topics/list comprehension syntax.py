
# square list for even numbers only in a range of 1-12
[x**2 for x in range(1,12) if (x) % 2 == 0]

# list of doubles for numbers divisible by three, range of 1-6
[x*2 for x in range(1,6) if (x*2) % 3 == 0]

# other comprehension list
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 ==0]
print cubes_by_four


# list slicing
l = [i ** 2 for i in range(1, 11)]
# will print  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
# will print [9, 25, 49, 81]
