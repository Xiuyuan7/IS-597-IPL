`combo_stuff_1` list is created as following. 

`combo_stuff_2` list is created by assigning `combo_stuff_1` list to it. 

When the first element of `combo_stuff_2` list is changed to `0`, the first element of `combo_stuff_1` list is also changed to `0`.

```python
combo_stuff_1 = [1, 7.23, ['Hello', 'World'], 'text']
combo_stuff_2 = combo_stuff_1
combo_stuff_2[0] = 0
```

If `combo_stuff_2` list is a shallow copy of `combo_stuff_1` list, they have the same id.

```python
print(id(combo_stuff_1), id(combo_stuff_2))
```

If both `combo_stuff_1` list and `combo_stuff_2` list are created separately, they will have different ids.

```python
combo_stuff_1 = [1, 7.23, ['Hello', 'World'], 'text']
combo_stuff_1 = [1, 7.23, ['Hello', 'World'], 'text']
print(id(combo_stuff_1), id(combo_stuff_2))
```

Lists contain only references while strings are objects. Strings are referred by references in a string list, so only lists have shallow copy problems but strings do not have.
