my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(my_list):
    soma_impares = 0
    for i in my_list:
        if i % 2 != 0:
            soma_impares += i
    return soma_impares
resultado = sum_odds(my_list)
print(sum_odds(my_list))