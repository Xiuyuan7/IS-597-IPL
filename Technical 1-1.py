data = ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']

numbers = []
text = []

for item in data:
    if isinstance(item, (int, float)):
        numbers.append(item)
    elif isinstance(item, str):
        text.append(item)
    else:
        print(f'{item} is not integer, float, or string.')

assert len(numbers) == 4, "length of numbers should be 4, but is " + str(len(numbers))
assert len(text) == 13, "length of text should be 13, but is " + str(len(text))

print(text)
print(numbers)
