
# square list for even numbers only in a range of 1-12
[x**2 for x in range(1,12) if (x) % 2 == 0]

# list of doubles for numbers divisible by three, range of 1-6
[x*2 for x in range(1,6) if (x*2) % 3 == 0]

# other comprehension list
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 ==0]
print cubes_by_four
