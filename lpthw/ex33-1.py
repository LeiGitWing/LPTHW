def while_loop(a):
    i = 0
    numbers = []
    while i < a:
        print(f"At the top is is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    
    return numbers

numbers = while_loop(3)
for num in numbers:
        print(num)
