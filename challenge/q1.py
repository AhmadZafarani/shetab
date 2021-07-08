upper_bound = 1000
multiplers = set()
for i in range(upper_bound):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        multiplers.add(i)
print(sum(multiplers))
