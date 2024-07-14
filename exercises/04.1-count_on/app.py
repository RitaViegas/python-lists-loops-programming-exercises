my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
for i in my_list:
    print(type(i))

new_list = []
for i in my_list:
    if isinstance(i, dict) or isinstance(i, list):
        new_list.append(i)
print(new_list)
