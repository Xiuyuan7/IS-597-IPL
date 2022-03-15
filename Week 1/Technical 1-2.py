data = ['a', 'B', '3.14', 'cat', 'dog', 2, 8, '9', 'foo', 'ten', 10.2, 'dog', 9.0, 'buzz', 'x', 'y', '1000']

numbers = []
text = []

for item in data:
    if isinstance(item, (int, float)):
        numbers.append(item)
    elif isinstance(item, str):
        item_clean = item.replace('.', '', 1)
        if item_clean.isdigit():
            numbers.append(float(item))
        else:
            text.append(item)
    else:
        print(f'{item} is not integer, float, or string.')

assert len(numbers) == 7, "length of numbers should be 7, but is " + str(len(numbers))
assert len(text) == 10, "length of text should be 10, but is " + str(len(text))

print(text)
print(numbers)
