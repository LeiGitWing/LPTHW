def for_loop(a, b):
    i = 0
    numbers = []

    for i in range(0, a, 2):
        print(f"At the top is is {i}")
        numbers.append(i)

        # i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers


print("The numbers:")
numbers = for_loop(6, 2)
for num in numbers:
    print(num)