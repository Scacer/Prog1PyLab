a_list = ["The next value is an int", 2, "and now a float", 6.3]
b_list = [25, 5, 10, 15, 50, 20, 30, 35, 40]

c_list = a_list + b_list

even_indx_c_list = c_list[1::2]

print(even_indx_c_list)

odd_indx_c_list = c_list[0::2]

print(odd_indx_c_list)