my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(my_list):
    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num

print(max_integer(my_list))