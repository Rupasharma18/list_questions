def second_max(number):
    i = 0
    max_num = number[0]
    sec_max = number[1]
    while i < len(number):
        if number[i] > max_num:
            max_num = number[i]
        else:
            if number[i] > sec_max:
                sec_max = number[i]    
        i = i +1
    return sec_max
numbers = [-50, -40, -23, -70, -56, -12, 5, 10, 7]    
print (second_max(numbers))         