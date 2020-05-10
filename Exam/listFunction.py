'''
alphabet = ["a", "b", "c", "d", "e", "f"]

print("리스트의 길이는: %d" % len(alphabet))



numbers = []

numbers.append(5)
print(numbers)

numbers.append(3)
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.insert(3, 12)
print(numbers)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]

del numbers[3]
print(numbers)

del numbers[4:]
print(numbers)

numbers = [6, 7, 10, 19, 212, 555, 1024, 15, 112, 1, 24, 22]

print(sorted(numbers))
'''

alphabet1 = ["a", "b", "c"]
alphabet2 = ["d", "e", "f"]
alphabet = alphabet1 + alphabet2

print(alphabet)